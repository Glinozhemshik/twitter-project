
from django.shortcuts import render, redirect, get_object_or_404
from twitterapp.models import Twit
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from twitterapp.forms import TwitForm

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
    return render(request, 'index.html', {"mess": contacts, "form":form})


def user(request, pk):
    if request.method == "GET":
        mess = Twit.objects.filter(user_id=pk)
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
        return render(request, 'edit.html', {'form': form})