from django import forms

class UploadFileForm(forms.Form):
	description = forms.CharField(label='Describe your file')
	file = forms.FileField(
			label='Select a file'
		)