from .views import Login, Registration
from django.urls import path

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('reg/', Registration.as_view(), name='registration'),
]
