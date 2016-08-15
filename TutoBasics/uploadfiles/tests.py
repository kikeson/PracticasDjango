from django.test import TestCase
from uploadfiles.models import Document
import os, TutoBasics
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import UploadFileForm
# Create your tests here.
class DocumentTestCase(TestCase):
    def setUp(self):
        Document.objects.create(description='First description',docfile='first.foo')
        Document.objects.create(description='Second description',docfile='second.foo')

    def test_we_can_retrieve_files(self):
        first = Document.objects.get(description='First description')
        second = Document.objects.get(description='Second description')

        self.assertEqual(first.docfile,'first.foo')
        self.assertEqual(second.docfile,'second.foo')


    def test_upload_form_works(self):
        name = 'prueba.csv'
        f = open(os.path.join(TutoBasics.settings.BASE_DIR,'documents',name),"rb")
        file_data = {'file':SimpleUploadedFile(f.name,f.read())}
        data = {'description':'rpue'}
        form = UploadFileForm(data,file_data)
        self.assertTrue(form.is_valid())

    def test_redirects_after_upload(self):
        pass