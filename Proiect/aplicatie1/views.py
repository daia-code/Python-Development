
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.models import Locations


class LocationsView(LoginRequiredMixin, ListView):
    model = Locations
    template_name = 'aplicatie1/locations_index.html'
    paginate_by = 5


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Locations
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Locations
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


@login_required
def delete_location(request, pk):
    Locations.objects.filter(id=pk).update(active=0)
    return redirect('locations:lista_locatii')


@login_required
def activate_location(request, pk):
    Locations.objects.filter(id=pk).update(active=1)
    return redirect('locations:lista_locatii')
