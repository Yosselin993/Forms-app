from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Login
from .forms import LoginForm

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template("index.html");
    return HttpResponse(template.render(context, request));

# def login(request):
#     email = request.POST["email"]
#     password = request.POST["password"]

#     if "@" not in email:
#         print("Invaild email")
#     Login.objects.create(email=email, password=password)

#     context = {"usersemail": email}
#     template = loader.get_template("index.html"); #changed
#     return HttpResponse(template.render(context, request));


def login(request):
    if request.method == "POST":
        #making django vaildate the emails 
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            #shows in terminal, no
            print("Form saved")
        else:
            print("Invaild Form")

        email = request.POST["email"];
        password = request.POST["password"];

    

        context = {"usersemail": email}
        template = loader.get_template("index.html"); #changed
        return HttpResponse(template.render(context, request));


def details(request):
    detailsList = Login.objects.all
    context = {"details": detailsList}
    template = loader.get_template("details.html");
    return HttpResponse(template.render(context, request));