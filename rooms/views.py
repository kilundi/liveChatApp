from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from.models import Room
@login_required
def rooms(request):
    user = request.user
    username = request.user.username
    is_active = user.is_active  # Check if the user is active
    rooms = Room.objects.all()
    return render(request,'rooms/rooms.html', {'rooms': rooms, 'username': username, 'is_active': is_active})

@login_required
def room(request,slug):
    user = request.user
    username = request.user.username
    is_active = user.is_active
    room = Room.objects.get(slug=slug)
    return render(request,'rooms/room.html', {'room': room, 'username': username, 'is_active': is_active})