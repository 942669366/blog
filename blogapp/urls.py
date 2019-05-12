from django.conf.urls import url
from blogapp import views
from blogapp.uploads import upload_image

urlpatterns = [
    url(r'^blog/(\d+)/$',views.blog),
    url(r'^$',views.blogg),
    url(r'^news/(\d+)/$',views.news),
    url(r'^test1/$',views.test1),
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
    url(r'^test/$',views.test),
    url(r'^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]