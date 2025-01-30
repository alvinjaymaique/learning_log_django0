from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')
        
def logged_out(request):
    """Logout user."""
    auth_logout(request=request)
    # return redirect('learning_logs:index')
    return render(request, 'users/logged_out.html')