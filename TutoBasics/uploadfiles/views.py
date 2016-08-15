from django.shortcuts import render
from .forms import UploadFileForm
from uploadfiles.models import Document
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os, TutoBasics
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