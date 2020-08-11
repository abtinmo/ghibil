from django.urls import include, path


urlpatterns = [
    path("", include([
        path(
            "movies/",
            include("ghibil.movies.api.v1.urls"),
            name="movies",
        ),
    ])),
]
