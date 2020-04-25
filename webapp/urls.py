from django.urls import path
from django.conf.urls import handler500

handler500 = 'webapp.views.error_500'
handler404 = 'webapp.views.error_404'


from . import views





urlpatterns = [
    path('', views.malurl_form, name='index'),
]
