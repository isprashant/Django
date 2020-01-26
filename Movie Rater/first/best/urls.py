from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'best'

urlpatterns = [
    path("movies", views.MovieList.as_view(), name='movielist'),
    path("movie/<int:pk>", views.MovieDetail.as_view(), name='moviedetail'),
    path('person/<int:pk>', views.PersonDetail.as_view(template_name='person_detail.html'),\
     name='persondetail'),
    path('movies/top', views.TopMovies.as_view(), name='topmovies'),
    path("movie/<int:movie_id>/vote", views.CreateVote.as_view(), name='createvote'),
    path("movie/<int:movie_id>/vote/<int:pk>", views.UpdateVote.as_view(), name='updatevote'),
    path('movie/<int:movie_id>/image/upload', views.MovieImageUpload.as_view(), name='movie-image-upload'),
    
]


