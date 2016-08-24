from django.shortcuts import render
from .forms import UploadFileForm
from uploadfiles.models import Document
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os, TutoBasics, html
# Create your views here.
def home_page(request):
    listfiles = Document.objects.all()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            newdoc = Document(description=request.POST['description'],docfile=request.FILES['file'])
            newdoc.save()
            listfiles = Document.objects.all()
            # Redirect to the document list after POST

            return HttpResponseRedirect("upload_ok/")    
            # return render(
            #     request,
            #     'home.html',
            #     {'form': form
            #         ,'upload_ok': 1
            #         ,'listfiles':listfiles  }
            # )
    else:
        form = UploadFileForm()
        # A empty, unbound form

    return render(
        request,
        'home.html',
        {'form': form, 'listfiles':listfiles}
    )

def upload_ok(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    return render(request,'upload_ok/')

def confirm_delete(request, datafile):
    docid = Document.objects.get(id=datafile)
    context = {"datafile" : datafile, "docid" : docid}
    if request.method == 'POST':
        if 'delete_ok' in request.POST:
            docid.delete()
        return HttpResponseRedirect('/uploadfiles')
    return render(request, 'confirm_delete/', context)

def load_document(request, datafile):
    docid = Document.objects.get(id=datafile) 
    lines = sum(1 for row in docid.docfile)  # fileObject is your csv.reader
    content_text = []
    if request.method == 'POST':
        if 'load_ok' in request.POST:
                docid.docfile.open(mode='r')
                content_text = docid.docfile.read().decode(errors='replace')
                print(type(content_text))
                content_text.replace("&","&amp;")
                html.escape(content_text)
                docid.docfile.close()
        else:
            return HttpResponseRedirect('/uploadfiles')
    context = {"datafile" : datafile, "docid" : docid, "lines" : lines, "content_text" : content_text}
    return render(request, 'load_document/', context)    