from django.conf.urls import url
from blogapp import views

urlpatterns = [
    url(r'^blog/(\d+)/$',views.blog),
    url(r'^news/(\d+)/$',views.news),
    # url(r'^admins/$',views.admins),
    url(r'^add/$',views.add),
    url(r'^addzan/(\d+)/$',views.addzan),
    url(r'^addlow/(\d+)/$',views.addlow),
    url(r'^addpin/(\d+)/$',views.addpin),
    url(r'^addblog/$',views.addblog),
    url(r'^comeon/$',views.comeon),
    url(r'^comecheck/$',views.comecheck),
    url(r'^addlogin/$',views.addlogin),
    url(r'^dele/(\d+)/$',views.dele),
]