from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    Success_url = reverse_lazy("login")

# Create your views here.
