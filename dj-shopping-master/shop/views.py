from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Serve Vue Application
landing = never_cache(TemplateView.as_view(template_name='index.html'))
