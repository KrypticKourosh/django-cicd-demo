from django.test import TestCase
from django.urls import reverse # imported but not used?

class HomeTest(TestCase):
    def test_home_status(self):
        response = self.client.get('/') # send a GET request using Django's internal client (for testing)
        self.assertEqual(response.status_code, 200)
