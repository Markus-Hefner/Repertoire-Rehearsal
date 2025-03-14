from . import views
from django.urls import path

urlpatterns = [
    # path('', views.SongList.as_view(), name='repertoire'),
    path('', views.song_list, name='repertoire'),
    path('<int:id>/', views.song_rehearsal, name='song_rehearsal'),
    path('<int:id>/edit/', views.song_edit, name='song_edit'),
]