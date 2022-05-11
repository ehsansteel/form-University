from django.shortcuts import render
# from .models import detaform


def home(request):


    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     password = request.POST.get("password")
    
    # username = detaform(name=name, password=password, email=email)
    # print(username)

    return render(request,"form_app/from.html")





     