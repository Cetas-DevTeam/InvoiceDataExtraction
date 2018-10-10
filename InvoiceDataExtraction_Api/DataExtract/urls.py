from django.urls import path
from . import views



urlpatterns = [
      path('',views.index,name='index'),
      path(r'DataExtract/(?P<slug>[-\w]+)/$',views.extract,name = 'extract')
      #r'^posts/(?P<slug>[-\w]+)/$'
]
