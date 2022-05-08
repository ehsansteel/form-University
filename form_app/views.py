from django.shortcuts import render



def home(request):
    return render(request,"form_app/from.html")





def formss(request):
    return render(request, "form_app/forms.html")
     
    name = request.git.git(name)
    password = request.git.git(password)
    email = request.git.git(email)
    detaform.objects.create(name=name , password=password , email=email)

    detaform = Detaform.objects.all()
     