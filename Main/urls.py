from django.urls import path
from Main import views

urlpatterns = [
    path('', views.index, name='index', ),
    path('search/', views.search_quote, name='search', ),
    path('quote/list/', views.show_list_quote, name='show_list_quote', ),
    path('quote/create/', views.create_quote, name='create_quote', ),
    path('quote/<int:quote_id>/show/', views.show_quote, name='show_quote', ),
    path('tag/list/', views.show_list_tag, name='show_list_tag', ),
    path('tag/<int:tag_id>/show/', views.show_tag, name='show_tag', ),
    path('author/list/', views.show_list_author, name='show_list_author', ),
    path('author/<int:author_id>/show/', views.show_author, name='show_author', ),
    path('403/', views.handler403, name='403', ),
    path('404/', views.handler404, name='404', ),
]
