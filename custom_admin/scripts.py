import os 
import django
import requests 
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custom_admin.settings')
django.setup()


from home.models import *
import random


fake = Faker(locale='en_IN')

def seeder(values):
    customer_instance = Customer.objects.all()
    statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']
    for i in range(values):
        customer = random.choice(customer_instance)     
        order_date = fake.date_this_year()
        total_amount = random.uniform(50, 500)
        status = random.choice(statuses)

        Order.objects.create(
            customer = customer,
            order_date = order_date,
            total_amount = total_amount,
            status = status
        )

seeder(100)


