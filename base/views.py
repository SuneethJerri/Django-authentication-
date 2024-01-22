from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import cache_control


@login_required
def home(request):
    profiles = User.objects.all()  # Query all users
    return render(request, 'home.html', {'profiles': profiles})


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   messages.success(request, 'Signed In Successfully!')
   return redirect("base:login")
 else:
  form = UserCreationForm()
  messages.error(request, 'Invalid username or password.')
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