"""
Definition of views.
"""

from datetime import datetime
from urllib.request import Request
from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    
    if request.method == "POST":
        username = request.POST['regNo']
        password = request.POST['smisPass']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request=request,user=user)
            print(user)
            messages.success(request,"You have been logged in successfully")
            return redirect('student')
        else:
            messages.success(request,"Error")
            return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('student')

        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
            )
def logout(request):
    auth.logout(request)
    messages.success(request,"You have been logged out successfully")
    return redirect('home')
   
@login_required
def student(request):
    """Renders the student page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/StudentDashboard.html',
        {
            'title':'Student Dashboard',
            'year':datetime.now().year,
        }
    )
@login_required
def studentGrades(request):
    """Renders the student page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/grades.html',
        {
            'title':'Student Grade',
            'year':datetime.now().year,
        }
    )
@login_required
def studentTranscript(request):
    """Renders the student page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/transcript.html',
        {
            'title':'Student Grade',
            'year':datetime.now().year,
        }
    )
@login_required
def profile(request):
    """Renders the student page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profile.html',
        {
            'title':'Student Profile',
            'year':datetime.now().year,
        }
    )
@login_required
def policy(request):
    """Renders the student page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/policy.html',
        {
            'title':'Policy',
            'year':datetime.now().year,
        }
    )
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
