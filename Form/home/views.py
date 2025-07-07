from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import person

# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        address = request.POST.get("address")
        profile_pic = request.FILES["upload_to"]

        person.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            address = address,
            gender = gender,
            age = age,
            profile_photo = profile_pic
        )

        return redirect("/thankyou/")
    
    return render(request, "formpage.html")

def thankyou(request):
    return render(request, "thankyoupage.html")