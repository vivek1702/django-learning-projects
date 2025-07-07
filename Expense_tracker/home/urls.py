
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view"),
    path('', index, name='index'),
    path('delete-transaction/<uuid>', deleteTransaction, name='deleteTransaction')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)