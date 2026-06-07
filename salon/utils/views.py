import re

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView

def crud_views(model_name, model_form_class, list_url_name, context_name):
    # Class names are given in camel-case. Detect the upper character,
    # add an underscore before it to match the template name
    folder = re.sub(r"(?<!^)(?=[A-Z])", "_", model_name.__name__).lower()

    # Note: making these generic might not be the best step after all
    # as in case of error "List" will be printed instead of CustomerListView for example.
    class List(ListView):
        model = model_name
        template_name = f"salon/{folder}/list.html"
        context_object_name = context_name

    class Create(CreateView):
        model = model_name
        form_class = model_form_class
        template_name = f"salon/{folder}/add.html"
        success_url = reverse_lazy(list_url_name)

    class Delete(DeleteView):
        model = model_name
        success_url = reverse_lazy(list_url_name)

    return List, Create, Delete