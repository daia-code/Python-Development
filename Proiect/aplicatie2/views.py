from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import Companies


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'
    paginate_by = 5


class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['nume', 'website', 'tip_companie']
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['nume', 'website', 'tip_companie']
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


@login_required
def delete_companies(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:lista_companii')


@login_required
def activate_companies(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:lista_companii')
