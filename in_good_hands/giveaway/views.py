from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, UpdateView, DetailView, View, DeleteView
# Create your views here.


class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")