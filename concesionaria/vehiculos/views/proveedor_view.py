from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from vehiculos.repositories.proveedor import ProveedorRepository
from vehiculos.models import Proveedor
from vehiculos.forms import ProveedorForm
from django.contrib.auth.mixins import UserPassesTestMixin

repo = ProveedorRepository()

class ProveedorListView(View):
    def get(self, request):
        proveedores = repo.get_all()
        return render(request, 'proveedor/list.html', {'proveedores': proveedores})

class ProveedorDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, id: int):
        proveedor = repo.get_by_id(id)
        repo.delete(proveedor)
        return HttpResponseRedirect(reverse('proveedor_list'))

class ProveedorUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, id: int):
        proveedor = get_object_or_404(Proveedor, id=id)
        form = ProveedorForm(instance=proveedor)
        return render(request, 'proveedor/update.html', {'form': form})

    def post(self, request, id: int):
        proveedor = get_object_or_404(Proveedor, id=id)
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('proveedor_list'))
        return render(request, 'proveedor/update.html', {'form': form})

class ProveedorCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        form = ProveedorForm()
        return render(request, 'vehiculos/create.html', {'form': form})

    def post(self, request):
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('proveedor_list'))
        return render(request, 'vehiculos/create.html', {'form': form})


class ProveedorDetailView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, id: int):
        proveedor = get_object_or_404(Proveedor, id=id)
        return render(request, 'proveedor/detail.html', {'proveedor': proveedor})
