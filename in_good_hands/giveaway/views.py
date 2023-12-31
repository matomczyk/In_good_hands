from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, CreateView, ListView, UpdateView, DetailView, View, DeleteView
from .models import Donation, Institution, User, Category


# Create your views here.


class LandingPage(View):
    def get(self, request):
        quantity = 0
        donations = list(Donation.objects.all())
        num_of_organizations = Institution.objects.count()
        fundations = []
        non_gov_organizations = []
        local = []
        for donation in donations:
            quantity += donation.quantity
            fundations = list(Institution.objects.filter(type=1))
            non_gov_organizations = list(Institution.objects.filter(type=2))
            local = list(Institution.objects.filter(type=3))
            categories_inst = list(Institution.categories.through.objects.all())
            categories = list(Category.objects.all())
        ctx = {"quantity": quantity,
               "organizations": num_of_organizations,
               "fundations": fundations,
               "non_gov": non_gov_organizations,
               "local": local,
               "categories_inst": categories_inst,
               "categories": categories}
        return render(request, "index.html", ctx)


class AddDonation(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "add-donation"

    def get(self, request):
        user = request.user
        name = user.first_name
        categories = list(Category.objects.all())
        return render(request, "form.html", {"user": user,
                                             "categories": categories})


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    @csrf_exempt
    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main-page')
        else:
            return render(request, 'register.html', {"message": "Login failed"})


class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')


class Register(View):
    def get(self, request):
        return render(request, "register.html")

    @csrf_exempt
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





class UserPage(LoginRequiredMixin, DetailView):
    pass
#     login_url = "/login/"
#
#     def get(self, request):
#         user = request.user
#         donations = list(Donation.objects.filter(user_id=user))
#         donation_categories = list(Donation.categories.through.objects.all())
#         donation_categories_list = []
#         categories = []
#         for donation in donations:
#             for category in donation_categories:
#                 if donation.id == category.donation_id:
#                     donation_categories_list.append(Category.objects.values_list("name", flat=True))
#         return render(request, "user-page.html", {"name": user.first_name,
#                                                   "surname": user.last_name,
#                                                   "email": user.email,
#                                                   "donations": donations,
#                                                   "categories": donation_categories_list})

