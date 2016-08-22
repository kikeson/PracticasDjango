from django.db import models

# Create your models here.
class Document(models.Model):
	description = models.CharField(default='',max_length=100)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')	
	deleted = models.BooleanField(default=False)

	def __str__(self):
		return "%s" % (self.description)
