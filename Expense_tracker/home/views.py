from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import *
from django.db.models import Sum

# Create your views here.

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


        Transaction.objects.create(
            description = description,
            amount = amount
        )

        return redirect('/')
    
    
    context = {'transactions': Transaction.objects.all(),
               'balance': Transaction.objects.aggregate(total_balance=Sum('amount'))['total_balance'],
               'income': Transaction.objects.filter(amount__gte = 0).aggregate(income_balance=Sum('amount'))['income_balance'],
               'expense': Transaction.objects.filter(amount__lte = 0).aggregate(expense_balance=Sum('amount'))['expense_balance']
               }

    return render(request, 'index.html', context)

def deleteTransaction(request, uuid):
    Transaction.objects.get(uuid = uuid).delete()
    return redirect('/')



