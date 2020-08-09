from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from web_service import get_movies


class MovieView(APIView):
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60))
    def get(self, request):
        return Response(
            {
                "results": get_movies(),
            },
        )
