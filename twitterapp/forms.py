# coding=utf-8
from django.forms import ModelForm
from twitterapp.models import Twit

class TwitForm(ModelForm):
    class Meta:
        model = Twit
        fields = ("text",)