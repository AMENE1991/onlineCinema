from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from CinemaApp.views import movies, FilmListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movies, name="movies"),
    path('movie_create/', FilmListCreate.as_view(), name="movie_create"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
