from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # UserProfile.objects.create(user=user, nickname=form.cleaned_data['nickname'], email=form.cleaned_data['email'], phone=form.cleaned_data['phone'], dob=form.cleaned_data['dob'], avatar=form.cleaned_data['avatar'])
            login(request, user)
            return redirect('user_info')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_info')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_info')
        else:
            return render(request, 'core/login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'core/login.html')

@login_required
def user_info(request):
    try:
        profile = get_object_or_404(UserProfile, user=request.user)
    except Exception as e:
        profile = None
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_info')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'core/user_info.html', {'form': form, 'profile': profile})

def user_logout(request):
    logout(request)
    return redirect('user_login')