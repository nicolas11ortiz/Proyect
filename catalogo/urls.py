from django.urls import path, include
from . import views 
from django.contrib import admin
from .views import juego, Genre, contacto, formulario, JuegoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('juegosap', JuegoViewSet)


urlpatterns = [ path('api/', include(router.urls)),
]

urlpatterns = [
    path('',views.index,name='index'),
    path('juego/', views.JuegoListView.as_view(), name='juego'),
    path('juego/<int:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', views.formulario, name='formulario'), 
    path('products/<str:id>/', views.products, name="products"),
   
    
]


urlpatterns += [
    path('genre/create/', views.genre_new,name='genre_create'),
    path('genre/<int:pk>/update/', views.genre_edit, name='genre_update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete'),
    path('juego/create/', views.juego_new,name='juego_create'),
    path('juego/<str:pk>/update/', views.juego_edit, name='juego_update'),
    path('juego/<str:pk>/delete/', views.JuegoDelete.as_view(), name='juego_delete'),
    
]

