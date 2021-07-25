from django.contrib.auth import authenticate, login, get_user_model
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, DeleteView, FormView,
    CreateView, UpdateView, TemplateView
)
