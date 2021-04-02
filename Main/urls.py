from django.urls import path
from Main import views

urlpatterns = [
    path('', views.index, name='index', ),
    path('quote/list/', views.quote_list, name='quote_list', ),
    path('quote/create/', views.quote_create, name='quote_create', ),
    path('tag/list/', views.tag_list, name='tag_list', ),
    path('tag/<int:tag_id>/show/', views.tag_show, name='tag_show', ),
    path('author/list/', views.author_list, name='author_list', ),
    path('author/<int:author_id>/show/', views.author_show, name='author_show', ),
]
