from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)