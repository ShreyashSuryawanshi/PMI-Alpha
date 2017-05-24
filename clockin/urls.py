from django.conf.urls import url
from .models import Work
from . import views

urlpatterns = [
    url(r'^$', views.work_list, name='index'),
    url(r'^(?P<work_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^home/$', views.work_list, name= 'home'),
    url(r'^start_shift/$', views.add_new, name= 'add'),
    url(r'^edit/(?P<work_id>\d+)/$', views.clockout, name='item_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.workDelete.as_view(model = Work), name="person_delete"),
    url(r'^test/$', views.WorkListView.as_view(), name="person_list_2"),
    url(r'^adminhome/$', views.AdminView, name= 'adminhome'),




]