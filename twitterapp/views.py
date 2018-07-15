import re

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from twitterapp.models import Twit
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from twitterapp.forms import TwitForm, EditProfile
from django.contrib.auth.models import User



def login(request):
    return render(request, 'account/login.html')




def form_twit(request):
    if request.method == "POST":
        form = TwitForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("/")

    else:

        form = TwitForm()
        mess = Twit.objects.all()
        paginator = Paginator(mess, 10)

        page = request.GET.get('page')
        contacts = paginator.get_page(page)
    return render(request, 'index.html', {"mess": contacts, "form": form})


def user(request, pk):
    if request.method == "GET":
        mess = Twit.objects.filter(Q(user_id=pk) | Q(re_twit=request.user))
        return render(request, 'user.html', {"mess": mess})


def edit_twit(request, pk):
    mess = get_object_or_404(Twit, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TwitForm(data=request.POST, instance=mess)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("/user/{}".format(request.user.id))
    else:
        form = TwitForm(instance=mess)
        return render(request, 'twit_edit.html', {'form': form})


def retwit(request, pk):
    mess = get_object_or_404(Twit, pk=pk)
    mess.re_twit.add(request.user)
    mess.save()
    return redirect("/")


def edit_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = EditProfile(data=request.POST, instance=user)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            match = re.match("^[a-z, A-Z]+\w+$", first_name)
            if match is not None:
                form.save()
            return redirect('/user/profile/'.format(request.user.id))
    else:
        form = EditProfile(instance=user)
        return render(request, 'profile.html', {'form': form})


def twit_single(request, pk):
    mess = get_object_or_404(Twit, pk=pk)
    if request.method == "POST":
        form = TwitForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.answers = mess
            form.save()
            return redirect("/message/{}".format(pk))
    else:
        answers = Twit.objects.filter(answers=mess)
        form = TwitForm()
    return render(request, "twit_answer.html", {"mess": mess,
                                                "form": form,
                                                "answers": answers})