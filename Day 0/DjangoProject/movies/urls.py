from django.urls import path
from . import views  # . specifies current directory

# empty string represents root
urlpatterns = [
    path('', views.index, name='index') # root,call function, name
]