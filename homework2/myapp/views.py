from django.shortcuts import render, get_object_or_404
from .models import User

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'myapp/profile.html', {'user': user})