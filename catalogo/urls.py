from django.urls import path 
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('juego/', views.JuegoListView.as_view(), name='juego'),
    path('juego/<int:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', views.formulario, name='formulario'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail'),
    path('juego/<str:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),
    
]

urlpatterns += [
    path('genre/create/', views.genre_new,name='genre_create'),
    path('genre/<int:pk>/update/', views.genre_edit, name='genre_update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete'),
    path('juego/create/', views.juego_new,name='juego_create'),
    path('juego/<str:pk>/update/', views.juego_edit, name='juego_update'),
    path('juego/<str:pk>/delete/', views.JuegoDelete.as_view(), name='juego_delete'),
]