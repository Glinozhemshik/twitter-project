# coding=utf-8
from django.forms import ModelForm
from twitterapp.models import Twit
from django.contrib.auth.models import User


class TwitForm(ModelForm):
    class Meta:
        model = Twit
        fields = ("text",)


class EditProfile(ModelForm):
    class Meta:
        model = User
        fields = ('first_name',)

