from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView  

from .models import Media

# Create your views here.

class HomeView(TemplateView):

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # to extend context adding new variab
        #context['test'] = "test-1"

        return context
    


class AboutView(TemplateView):

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class ContactView(TemplateView):

    template_name = "main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


class MediaView(ListView):

    template_name = "main/contact.html"
    model = Media

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context