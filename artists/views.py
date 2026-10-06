from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from . import models


def index(request: HttpRequest):
    return HttpResponse("HELLO WORLD")

def artists_page(request: HttpRequest):
    artists = models.Artists.objects.all()

    context = {
        "artists": artists
    }
    return render(request, "all_artists.html", context=context)

# Selects an artist and renders their albums on a page
def select_artist(request: HttpRequest, art_id: int):
    artist = get_object_or_404(models.Artists, pk=art_id)
    albums = models.Albums.objects.filter(artist=artist)

    context = {
        "albums": albums,
    }
    return render(request, "all_albums.html", context=context)

# Selects an album and renders its songs on a page
def select_album(request: HttpRequest, art_id: int, alb_id: int):
    album = get_object_or_404(models.Albums, pk=alb_id)
    songs = models.Songs.objects.filter(album=album).order_by("album_pos")

    context = {
        "songs": songs,
    }
    return render(request, "album.html", context=context)