from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from home.models import *
from django.db.models import Sum, Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(Q(email=email) | Q(username=username))

        if user_obj.exists():
            messages.error(request, "email already exists !")
            return redirect("/register/")
        else:
            user_obj = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email
            )
            user_obj.set_password(password)
            user_obj.save()
            
            messages.error(request, "Account Created: Successfully")
            return redirect("/login/")


    return render(request, "Registration.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(
          username = username
            )
        if not user_obj.exists():
            messages.error(request, 'Error: Username does not exist')
            return redirect('/login/')

       
        user_obj = authenticate(username = username , password = password)

        if not user_obj:
            messages.error(request, 'Error: Invalid credentials')
            return redirect('/login/')
        
        login(request, user_obj)
        return redirect('/')
        

    return render(request , 'login.html')


def logout_view(request):
    logout(request)
    render(request, "logout.html")
    return redirect("/login/")

@login_required(login_url="/login/")
def index(request):

    if request.method == "POST":

        description = request.POST.get('description')
        amount = request.POST.get('amount')
        # print(description, amount)

        if not description:
            messages.info(request, "description cannot be blank")
            return redirect('/')
        
        # if amount.isdigit() == str:
        #     messages.info(request, "amount value should be number")
        #     return redirect('/')

        try:
            amount = float(amount)
        except(ValueError, TypeError):
            messages.info(request, "amount value should be number")
            return redirect('/')


        Transaction_table.objects.create(
            description = description,
            amount = amount,
            created_by = request.user
        )

        return redirect('/')
    
    
    context = {'transactions': Transaction_table.objects.filter(created_by = request.user),
               'balance': Transaction_table.objects.filter(created_by = request.user).aggregate(total_balance=Sum('amount'))['total_balance'],
               'income': Transaction_table.objects.filter(created_by = request.user, amount__gte = 0).aggregate(income_balance=Sum('amount'))['income_balance'],
               'expense': Transaction_table.objects.filter(created_by = request.user, amount__lte = 0).aggregate(expense_balance=Sum('amount'))['expense_balance']
               }

    return render(request, 'index.html', context)

def deleteTransaction(request, uuid):
    Transaction_table.objects.get(uuid = uuid).delete()
    return redirect('/')



