from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import *


# Create your views here.

class IndexView(generic.ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        if self.request.GET.get('category', None):
            return Category.objects.filter(category_name=self.request.GET['category'])
        return Category.objects.all()