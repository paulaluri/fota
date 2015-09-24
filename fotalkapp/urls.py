from django.conf.urls import url

#Route all URLs to app's router
urlpatterns = [
    url(r'^$', 'fotalkapp.views.home', name='home'),

    url(r'^post$', 'fotalkapp.views.post', name='post'),

    #Handle authentication
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^register$', 'fotalkapp.views.register', name='register'),
]
