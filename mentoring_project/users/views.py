from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    creation_date = user_profile.created_at.strftime('%m/%d/%Y')

    context = {
        'creation_date': creation_date,
        'last_failed_login': user_profile.last_failed_login
    }

    return render(request, 'users/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


