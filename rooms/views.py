from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from.models import Room

@login_required

def rooms(request):
    username = request.user.username
    rooms = Room.objects.all()
    return render(request,'rooms/rooms.html', {'rooms': rooms, 'username': username})