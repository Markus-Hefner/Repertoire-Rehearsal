from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='repertoire'),
    path('<int:id>/', views.song_rehearsal, name='song_rehearsal'),
    path('<int:id>/edit/', views.song_edit, name='song_edit'),
    path('<int:id>/delete_warning/', views.song_delete_warning, name='song_delete_warning'),
    path('<int:id>/delete/', views.song_delete, name='song_delete'),
]