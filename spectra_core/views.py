from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from spectra_core.models import Work
import json
import requests
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from spectra_core.models import Work, Author, Keyword
from django.contrib.auth.decorators import login_required
from .models import Work
from .forms import WorkForm  # assuming you have a form for Work
from django.shortcuts import redirect

def index(request):
    # View all works
    works = Work.objects.all()
    for work in works:
        print(work.title)
    
    return render(request, 'index.html', {'works': works})

# See work detail
def work(request, work_id):
    # Load a specific work
    work = Work.objects.get(id=work_id)
    return render(request, 'work.html', {'work': work})

# Create a new work


@login_required
def create_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.save()

            authors = form.cleaned_data['authors'].split(',')
            for author_name in authors:
                author, created = Author.objects.get_or_create(name=author_name.strip())
                work.authors.add(author)

            keywords = form.cleaned_data['keywords'].split(',')
            for keyword_name in keywords:
                keyword, created = Keyword.objects.get_or_create(name=keyword_name.strip())
                work.keywords.add(keyword)

            return redirect('work_detail', pk=work.pk)

    else:
        form = WorkForm()  # instantiate the form here

    return render(request, 'spectra_core/work_edit.html', {'form': form})

# Upon successful creation of a work
def create_work_success(request):
    return render(request, 'create_work_success.html')

# Remove all works DO NOT USE IN PRODUCTION
def delete_all_works(request):
    Work.objects.all().delete()
    return HttpResponseRedirect('/')

# Search for works using keywords
def search(request):
    search_term = request.GET.get('q')
    if search_term:
        works = Work.objects.filter(Q(title__icontains=search_term))
    else:
        works = Work.objects.all()
    return render(request, 'search_results.html', {'results': works})

def login(request):
    return render(request, 'login.html')

def handle_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def handle_create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            User.objects.create_user(username, password=password)
            return HttpResponse('Account created successfully.')
    return HttpResponse('Account creation failed.')

def create_account(request):
    return render(request, 'create_account.html')