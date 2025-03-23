from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class RateLimitTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.force_authenticate(user=self.user)

    def test_rate_limit(self):
        url = '/api/tasks/rate-limited/'
        for _ in range(6):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 429)  # Expect rate limit exceeded
