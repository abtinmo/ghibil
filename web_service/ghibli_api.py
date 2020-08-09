from logging import getLogger

import requests

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


logger = getLogger("ghibli_web_service")
BASE_URL = "https://ghibliapi.herokuapp.com/"


def get_movies():
    is_success, movies = request_handler("films")
    if not is_success:
        raise APIException(detail=_("Invalid response from upstream"))
    is_success, people = request_handler("people")
    people = people if is_success else []
    for movie in movies:
        movie["people"] = [
            people_item for people_item in people
            for film in people_item["films"] if film.endswith(movie["id"])
        ]
    return movies


def request_handler(end_point):
    try:
        return True, requests.get(BASE_URL + end_point).json()
    except requests.RequestException as ex:
        logger.error(str(ex))
        return False, str(ex)
