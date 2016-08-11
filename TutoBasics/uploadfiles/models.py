from django.db import models

# Create your models here.
class Document(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')	

	def __str__(self):
		return "%s" % (self.docfile.name)
