from django.urls import path
from.import views
app_name='mainapp'
urlpatterns=[
    path("",views.blogs,name='blogs'),
    path("blog/<int:id>/",views.blog,name='blog'),
    path("create_blog",views.create_blog,name='create_blog'),
    path("searchblog",views.searchblog,name='searchblog'),
    path("profile/<int:pk>/",views.profile,name='profile'),
    path("editblog/<int:pk>/",views.editblog,name='editblog'),
    path("deleteblog/<int:pk>/",views.deleteblog,name='deleteblog'),
    path("updateprofile",views.updateprofile,name='updateprofile'),
]