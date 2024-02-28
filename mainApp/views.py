from django.shortcuts import render

# Create your views here.
def home(Request):
    return render(Request,"index.html")

def about(Request):
    return render(Request,"about.html")

def service(Request):
    return render(Request,"service.html")

def project(Request):
    return render(Request,"project.html")

def projectSingle(Request):
    return render(Request,"project-single.html")

def rent(Request):
    return render(Request,"rent.html")

def team(Request):
    return render(Request,"team.html")

def gallery(Request):
    return render(Request,"gallery.html")

def contact(Request):
    return render(Request,"contact.html")