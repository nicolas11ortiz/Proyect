from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


# Create your models here.
class Genre(models.Model):
    #Model representing a book genre."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Juego(models.Model):
    
	title = models.CharField(max_length=200)
	Desarrolladora = models.ForeignKey('Desarrolladora', on_delete=models.SET_NULL, null=True)
	Plataforma = models.ForeignKey('Plataforma', on_delete=models.SET_NULL, null=True)

	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the juego')
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre)
	
	
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('juego-detail', args=[str(self.id)])



class Desarrolladora(models.Model):
	"""Model representing an author."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name	

class Plataforma(models.Model):
	"""Model representing an author."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name