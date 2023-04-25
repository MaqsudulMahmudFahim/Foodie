from django.shortcuts import render
from myapp.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        message= request.POST.get("message")

        obj = Contact(name=name, email=email, message=message)
        obj.save()
        context['message']=f"Dear {name}, Thanks for your time!"

    return render(request,'contact.html',context)