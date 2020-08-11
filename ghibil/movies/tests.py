from django.core.cache import cache
from rest_framework.test import APITestCase


class MovieTestCase(APITestCase):

    def test_get_movies(self):
        cache.delete_pattern("*")
        cache_before_request = len(cache.keys("*"))
        response = self.client.get(
            "/movies/", format="json",
        )
        self.assertEqual(response.status_code, 200)
        cache_after_request = len(cache.keys("*"))
        self.assertGreater(cache_after_request, cache_before_request)
