from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # Homepage
    path("artists/", views.artists_page, name="artist_page"), # All artist page
    # path("artists/<int:art_id>/albums/", views.select_artist, name="select_artist"), # Albums page for artist
    # path("artists/<int:id>/albums/<int:id>/", views.select_album, name="select_album"), # Specific album page
]
