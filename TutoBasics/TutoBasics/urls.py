
from django.conf.urls import include,url
from django.contrib import admin
from uploadfiles import views as upload_views
from uploadfiles import urls as upload_urls
urlpatterns = [
#	url(r'^$', upload_views.home_page,name='home'),
	url(r'^uploadfiles/', include(upload_urls)),
#    url(r'^admin/', admin.site.urls),
]
