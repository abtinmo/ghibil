from django.urls import include, path


urlpatterns = [
    path("api/v1/", include([
        path(
            "movies/",
            include("ghibil.movies.api.v1.urls"),
            name="movies",
        ),
    ])),
]
