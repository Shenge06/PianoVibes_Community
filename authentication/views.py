from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import Post

# Create your views here.

def home(request):
    """
    View function for the home page.
    """
    return render(request, "authentication/index.html")

@csrf_protect
def signup(request):
    """
    View function for user signup.
    """
    if request.method == "POST":
        # Retrieve form data
        username = request.POST.get('username', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        pass1 = request.POST.get('pass1', '')
        pass2 = request.POST.get('pass2', '')

        if username and fname and lname and email and pass1 and pass2:
            if pass1 == pass2:
                # Check if username already exists
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username is already taken")
                    return redirect("signup")
                
                # Create the user
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()

                messages.success(request, "Your account has been successfully created")
                return redirect("home")

            else:
                messages.error(request, "Passwords do not match")
                return redirect("signup")
        else:
            messages.error(request, "Please fill in all required fields")
            return redirect("signup")

    return render(request, "authentication/signup.html")

@csrf_protect
def signout(request):
    """
    View function for user signout.
    """
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

@csrf_protect
def signin(request):
    """
    View function for user signin.
    """
    if request.method == 'POST':
        print(request.POST)  # Add this line for debugging
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        if username and pass1:  # Check if both username and pass1 are not None
            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                fname = user.first_name
                return render(request, "authentication/index.html", {'fname': fname, 'user': user})

            else:
                messages.error(request, "Bad Credentials!")
                return redirect('home')
        else:
            messages.error(request, "Username or password is missing!")
            return redirect('home')

    return render(request, "authentication/signin.html")

def user_posts(request):
    """
    View function to display user's posts.
    """
    posts = Post.objects.filter(user=request.user)
    return render(request, 'authentication/user_posts.html', {'posts': posts})

def create_post(request):
    """
    View function for creating a new post.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(user=request.user, title=title, content=content)
            return redirect('user_posts')
    return render(request, 'authentication/create_post.html')

def about(request):
    """
    View function for the about page.
    """
    return render(request, 'authentication/about.html')

def contact(request):
    """
    View function for the contact page.
    """
    return render(request, 'authentication/contact.html')
