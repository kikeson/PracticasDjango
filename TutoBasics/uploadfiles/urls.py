
from django.conf.urls import url
from uploadfiles import views 

urlpatterns = [
	url(r'^$', views.home_page,name='home'),
	url(r'^upload_ok/$', views.upload_ok, name='upload_ok'),		
	url(r'^confirm_delete/([0-9]+)/$', views.confirm_delete, name='confirm_delete'),		
#    url(r'^admin/', admin.site.urls),
	
]
