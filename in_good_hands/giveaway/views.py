from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, UpdateView, DetailView, View, DeleteView
from .models import Donation, Institution, User
# Create your views here.


class LandingPage(View):
    def get(self, request):
        quantity = 0
        donations = list(Donation.objects.all())
        organizations = Institution.objects.count()
        for donation in donations:
            quantity += donation.quantity

        ctx = {"quantity": quantity,
               "organizations": organizations}
        return render(request, "index.html", ctx)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")

class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.last_name = surname
            user.save()
            return redirect('login')
        return render(request, 'register.html', {"message": "Hasła nie są takie same"})

