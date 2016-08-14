
from django.conf.urls import url
from uploadfiles import views 

urlpatterns = [
	url(r'^upload_ok/$', views.upload_ok, name='upload_ok'),		
#    url(r'^admin/', admin.site.urls),
	
]
