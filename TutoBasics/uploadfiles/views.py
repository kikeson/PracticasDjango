from django.shortcuts import render
from .forms import UploadFileForm
from uploadfiles.models import Document
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['file'])
            newdoc.save()

            # Redirect to the document list after POST
            return render(
                request,
                'home.html',
                {'form': form
                    ,'upload_ok': 1  }
            )
    else:
        form = UploadFileForm()
        # A empty, unbound form

    return render(
        request,
        'home.html',
        {'form': form}
    )