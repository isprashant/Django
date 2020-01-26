from django import forms
from django.contrib.auth import get_user_model
from best.models import Vote, Movie, MovieImage


class VoteForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput,
                                  queryset=get_user_model().objects.all(),
                                  disabled=True)
    movie = forms.ModelChoiceField(widget=forms.HiddenInput,
                                   queryset=Movie.objects.all(),
                                   disabled=True)

    value = forms.ChoiceField(widget=forms.RadioSelect, choices=Vote.CHOICES)  # lable='Vote',

    class Meta():
        model = Vote
        fields = ('value', 'user', 'movie')

class MovieImageForm(forms.ModelForm):

    movie = forms.ModelChoiceField(widget=forms.HiddenInput,
                                  queryset=Movie.objects.all(),
                                  disabled=True)
    user = forms.ModelChoiceField(widget=forms.HiddenInput,
                                queryset=get_user_model().objects.all(),
                                disabled=True)

    class Meta:
        model = MovieImage
        fields = ('image', 'user', 'movie')