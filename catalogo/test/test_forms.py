from django.test import TestCase
from catalogo.forms import GenreForm
from catalogo.models import juego
from django.core.files.uploadedfile import SimpleUploadedFile

class GenreFormsTest(TestCase):
    def test_valid_form(self):
        g = juego.objects.create(title='Prueba1', isbn='Prueba')
        data = {'title': g.title, 'isbn': g.isbn,}
        form = GenreForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Genre.objects.create(title='', isbn='Prueba')
        data = {'title': g.title, 'isbn': g.isbn,}
        form = GenreForm(data=data)
        self.assertFalse(form.is_valid())


