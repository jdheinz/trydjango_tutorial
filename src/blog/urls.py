from django.urls import path, re_path
from blog.views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view     
)

urlpatterns = [
    
    path('', blog_post_list_view),
    path('<str:slug>/', blog_post_detail_view), # represents same value below
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),
    #re_path(r'^blog/(?P<slug>\w+)/$', blog_post_detail_page), # represents same value above
]
