from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('videos', views.videos,name='videos'),
    path('post', views.post,name='post'),
    path('success', views.success,name='success'),
    path('blog/', views.blog,name='blog'),
    path('blog/post/', views.post,name='post'),
    path('blog/<slug:url>', views.post,name='post'),
    path('Category/<slug:url>',views.category,name='Category'),
    path('search', views.search,name='search'),
 ]