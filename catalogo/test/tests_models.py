from django.test import TestCase

# Create your tests here.
class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_title_label(self):
        juego=juego.objects.get(id=1)
        field_label = juego._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')    

     def test_title_max_length(self):
        juego=juego.objects.get(id=1)
        max_length = juego._meta.get_field('title').max_length
        self.assertEquals(max_length,200)


def test_isbn_label(self):
        juego=juego.objects.get(id=1)
        field_label = juego._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label,'isbn')    

     def test_isbn_max_length(self):
        juego=juego.objects.get(id=1)
        max_length = juego._meta.get_field('isbn').max_length
        self.assertEquals(max_length,13)
