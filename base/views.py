from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import cache_control
from .forms import ChangeUsernameForm
from .forms import UserCreationWithEmailForm

@login_required
def home(request):
    profiles = User.objects.all()  # Query all users
    return render(request, 'home.html', {'profiles': profiles})


def authView(request):
    if request.method == "POST":
        form = UserCreationWithEmailForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signed In Successfully!')
            return redirect("base:login")
    else:
        form = UserCreationWithEmailForm()
    return render(request, "registration/signup.html", {"form": form})

@cache_control(no_cache=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    response = redirect('base:login')
    response['Cache-Control'] = 'no-store'  # Ensure the response is not stored in the cache
    return response

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('base:home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            request.user.username = new_username
            request.user.save()
            messages.success(request, 'Username changed successfully.')
            return redirect('base:profile')  # Redirect to the profile page
    else:
        form = ChangeUsernameForm()

    return render(request, 'change_username.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update the session with the new password
            messages.success(request, 'Password changed successfully.')
            return redirect('base:profile')  # Redirect to the profile page
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})