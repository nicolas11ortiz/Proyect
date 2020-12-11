from django.shortcuts import render
from .models import Juego, Desarrolladora, Genre, Plataforma
from django.views import generic 
from rest_framework import viewsets
from .serializers import JuegoSerializer


class JuegoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Juego.objects.all()
    serializers_class = JuegoSerializer



# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_juegos=Juego.objects.all().count()
    # Libros disponibles (status = 'a')
    
    num_Desarrolladora=Desarrolladora.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_juegos':num_juegos,'num_Desarrolladora':num_Desarrolladora},
    )
def juego(request):
    num_juegos=Juego.objects.all()
    
    return render(
        request,
        'juego.html',
        context={'num_juegos':num_juegos},
    )
def contacto(request):
     return render(
        request,
        'contacto.html',
        
    )

def formulario(request):
    
    return render(
        request,
        'formulario.html',
    )


class JuegoListView(generic.ListView):
    model = Juego
    paginate_by = 10
class JuegoDetailView(generic.DetailView):
    model = Juego






    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic


class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('index')


class GenreDetailView(generic.DetailView):
    model = Genre
    
class JuegoDelete(DeleteView):
    model = Juego
    success_url = reverse_lazy('index')
    
class JuegoDetailView(generic.DetailView):
    model = Juego

class GenreListView(generic.ListView):
    model = Genre
    template_name = 'templates/catalogo/genre_list.html'
    queryset = Genre.objects.all()

    paginate_by = 10

def genre_new(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('genre-detail', pk=post.pk)
    else:
        form = GenreForm()
        return render(request, 'catalogo/genre_form.html', {'form': form})

def genre_edit(request, pk):
    post = get_object_or_404(Genre, pk=pk)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('genre-detail', pk=post.pk)
    else:
        form = GenreForm(instance=post)
    return render(request, 'catalogo/genre_form.html', {'form': form})

def juego_new(request):
    if request.method == "POST":
        form = JuegoForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #form.save_m2m()
            return redirect('juego-detail', pk=post.pk)
    else:
        form = JuegoForm()
        return render(request, 'catalogo/juego_form.html', {'form': form})

def juego_edit(request, pk):
    post = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        form = JuegoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('juego-detail', pk=post.pk)
    else:
        form = JuegoForm(instance=post)
    return render(request, 'catalogo/juego_form.html', {'form': form})