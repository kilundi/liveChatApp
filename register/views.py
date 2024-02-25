from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'register/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'register/signup.html', {'form': form})