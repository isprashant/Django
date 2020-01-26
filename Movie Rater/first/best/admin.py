from django.contrib import admin
from .models import Movie, Role, Person, Vote, MovieImage
from .forms import VoteForm
# Register your models here.

admin.site.register(Movie)
admin.site.register(Role)
admin.site.register(Person)
admin.site.register(Vote)
admin.site.register(MovieImage)

