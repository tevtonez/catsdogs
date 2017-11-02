from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from main import views as main_views

from django.conf.urls.static import static
from django.conf import settings
from catsdogs_api import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.IndexView.as_view(), name='home'),
    url(r'^main/$', main_views.mainIndexView.as_view(), name='main'),

    # logging users in/out
    url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    #signup users
    url(r'signup/$', main_views.SignUpView.as_view(),name = 'signup'),

    #api
    url(r'^api/', include('catsdogs_api.urls')),

]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
