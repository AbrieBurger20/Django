from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def homepage(request):
    """
    This view function handles the homepage.

    :param HttpRequest request: The HTTP request object.
    :returns: Renders the homepage if the user is authenticated, otherwise redirects to the signin page.
    :rtype: HttpResponse
    """
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return redirect('signin.html')

def drinks(request):
    """
    This view function handles the drinks page.

    :param HttpRequest request: The HTTP request object.
    :returns: Renders the drinks page.
    :rtype: HttpResponse
    """
    return render(request, 'drinks.html')

def food(request):
    """
    This view function handles the food page.

    :param HttpRequest request: The HTTP request object.
    :returns: Renders the food page.
    :rtype: HttpResponse
    """
    return render(request, 'food.html')

def signin(request):
    """
    This view function handles the signin page.

    :param HttpRequest request: The HTTP request object.
    :returns: Renders the signin form for GET requests and processes login for POST requests. Redirects to the homepage upon successful login.
    :rtype: HttpResponse
    """
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
    """
    This view function handles the goodbye page.

    :param HttpRequest request: The HTTP request object.
    :returns: Renders the goodbye page.
    :rtype: HttpResponse
    """
    return render(request, 'goodbye.html')

def signup(request):
    """
    This view function handles the signup page.

    :param HttpRequest request: The HTTP request object.
    :returns: Renders the signup form for GET requests and processes user registration for POST requests. Redirects to the homepage upon successful registration.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})