from django.urls import path
from Main import views

urlpatterns = [
    path('', views.index, name='index', ),
    path('quote/list/', views.quote_list, name='quote_list', ),
    path('subject/list/', views.subject_list, name='subject_list', ),
    path('author/list/', views.author_list, name='author_list', ),
]
