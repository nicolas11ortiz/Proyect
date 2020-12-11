from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from juegos.models import Genre, juegos

class GenreListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_genre = 13

        for genre_id in range(number_of_genre):
            Genre.objects.create(
                name=f'Accion {genre_id}',
                
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/genres/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo/genre_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['genre_list']) == 10)

    def test_lists_all_genres(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('genres')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['genre_list']) == 3)

class JuegoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_juego = 13
        g =Genre.objects.create(title='GTA V', isbn='001)

        for juego_id in range(number_of_juego):
            test_juego = Juego.objects.create(
                title=f'GTA V {juego_id}',
                genre= accion,
                url=f'Prueba.com {juego_id}',
                image= document
            )
            
            test_juego.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/juegos/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('juegos'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('juegos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'juegos.html')
        
 