from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return redirect('signin.html')

def drinks(request):
    return render(request, 'drinks.html')

def food(request):
    return render(request, 'food.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Corrected function call
            return redirect('homepage')  
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid credentials'})
    
    # For GET requests, render the signin form
    return render(request, 'signin.html')

# def welcome(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('homepage')
#     else:
#         form = UserCreationForm()
#     return render(request, 'welcome.html', {'form': form})

def goodbye(request):
    return render(request, 'goodbye.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})