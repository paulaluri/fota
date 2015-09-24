from django.conf.urls import include, url

#Route all URLs to app's router
urlpatterns = [
    url(r'^', include('fotalkapp.urls')),
]
