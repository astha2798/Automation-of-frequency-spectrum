from django.conf.urls import  url
from django.conf.urls import url
from . import views

urlpatterns = [
# path('', views.index, name='index'),
	url(r'^index/', views.index),
	url(r'^register/', views.register),
	url(r'^grant/', views.grant),
	url(r'^otp/', views.otp),
	url(r'^register_q/', views.register_q),
	# url(r'^model/', views.model),)

    url(r'^login_grant/', views.login_grant, name='login'),
    url(r'^login_logs/', views.login_logs, name='login'),
    url(r'^hatamodel/', views.hatamodel),
    url(r'^login_headq/', views.login_headq, name='login'),

    url(r'^costmodel/', views.costmodel),
    url(r'^costmodel_calc/', views.costmodel_calc),
    url(r'^hatamodel_calc/', views.hatamodel_calc),

    url(r'^pathloss/', views.pathloss, name='login'),
    url(r'^power_rec/', views.power_rec, name='login'),
	# url(r'^getMoreDetails/', views.getMoreDetails),
	# url(r'^add/', views.add),
	# url(r'^list/',views.list),
	# url(r'^edit/',views.edit),
	# url(r'^status/list/',views.statusList),
	# url(r'^exportCsv/',views.exportCsv),
	# url(r'^comment/add/',views.add_comment),
	# url(r'^history/view/',views.view_history),
	# url(r'^track/update/',views.updateTrack),
	# url(r'^track/',views.track),
]
