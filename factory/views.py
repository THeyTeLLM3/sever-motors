from django.shortcuts import render
from django.db.models.deletion import ProtectedError
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import (
    VehicleCategory,
    Workshop,
    Supplier,
    Vehicle,
    Part,
    Employee,
    ProductionOrder,
    QualityCheck,
)
from .forms import (
    VehicleCategoryForm,
    WorkshopForm,
    SupplierForm,
    VehicleForm,
    PartForm,
    EmployeeForm,
    ProductionOrderForm,
    QualityCheckForm,
)



def home(request):
    return render(request, "factory/home.html")


def about(request):
    return render(request, "factory/about.html")


def contacts(request):
    return render(request, "factory/contacts.html")


def directions(request):
    return render(request, "factory/directions.html")


def production(request):
    return render(request, "factory/production.html")

class ProtectedDeleteMixin:
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            context = self.get_context_data(form=form)
            context['delete_error'] = 'Р—Р°РїРёСЃСЊ РёСЃРїРѕР»СЊР·СѓРµС‚СЃСЏ РІ РґСЂСѓРіРёС… С‚Р°Р±Р»РёС†Р°С…. РЎРЅР°С‡Р°Р»Р° РёР·РјРµРЅРёС‚Рµ РёР»Рё СѓРґР°Р»РёС‚Рµ СЃРІСЏР·Р°РЅРЅС‹Рµ Р·Р°РїРёСЃРё.'
            return self.render_to_response(context)


class VehicleCategoryListView(ListView):
    model = VehicleCategory
    template_name = 'factory/categories/list.html'
    context_object_name = 'items'


class VehicleCategoryDetailView(DetailView):
    model = VehicleCategory
    template_name = 'factory/categories/detail.html'


class VehicleCategoryCreateView(CreateView):
    model = VehicleCategory
    template_name = 'factory/categories/form.html'
    form_class = VehicleCategoryForm
    success_url = reverse_lazy('factory:category_list')


class VehicleCategoryUpdateView(UpdateView):
    model = VehicleCategory
    template_name = 'factory/categories/form.html'
    form_class = VehicleCategoryForm
    success_url = reverse_lazy('factory:category_list')


class VehicleCategoryDeleteView(ProtectedDeleteMixin, DeleteView):
    model = VehicleCategory
    template_name = 'factory/categories/confirm_delete.html'
    success_url = reverse_lazy('factory:category_list')


class WorkshopListView(ListView):
    model = Workshop
    template_name = 'factory/workshops/list.html'
    context_object_name = 'items'


class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'factory/workshops/detail.html'


class WorkshopCreateView(CreateView):
    model = Workshop
    template_name = 'factory/workshops/form.html'
    form_class = WorkshopForm
    success_url = reverse_lazy('factory:workshop_list')


class WorkshopUpdateView(UpdateView):
    model = Workshop
    template_name = 'factory/workshops/form.html'
    form_class = WorkshopForm
    success_url = reverse_lazy('factory:workshop_list')


class WorkshopDeleteView(ProtectedDeleteMixin, DeleteView):
    model = Workshop
    template_name = 'factory/workshops/confirm_delete.html'
    success_url = reverse_lazy('factory:workshop_list')


class SupplierListView(ListView):
    model = Supplier
    template_name = 'factory/suppliers/list.html'
    context_object_name = 'items'


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'factory/suppliers/detail.html'


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'factory/suppliers/form.html'
    form_class = SupplierForm
    success_url = reverse_lazy('factory:supplier_list')


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'factory/suppliers/form.html'
    form_class = SupplierForm
    success_url = reverse_lazy('factory:supplier_list')


class SupplierDeleteView(ProtectedDeleteMixin, DeleteView):
    model = Supplier
    template_name = 'factory/suppliers/confirm_delete.html'
    success_url = reverse_lazy('factory:supplier_list')


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'factory/vehicles/list.html'
    context_object_name = 'items'


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'factory/vehicles/detail.html'


class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'factory/vehicles/form.html'
    form_class = VehicleForm
    success_url = reverse_lazy('factory:vehicle_list')


class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'factory/vehicles/form.html'
    form_class = VehicleForm
    success_url = reverse_lazy('factory:vehicle_list')


class VehicleDeleteView(ProtectedDeleteMixin, DeleteView):
    model = Vehicle
    template_name = 'factory/vehicles/confirm_delete.html'
    success_url = reverse_lazy('factory:vehicle_list')


class PartListView(ListView):
    model = Part
    template_name = 'factory/parts/list.html'
    context_object_name = 'items'


class PartDetailView(DetailView):
    model = Part
    template_name = 'factory/parts/detail.html'


class PartCreateView(CreateView):
    model = Part
    template_name = 'factory/parts/form.html'
    form_class = PartForm
    success_url = reverse_lazy('factory:part_list')


class PartUpdateView(UpdateView):
    model = Part
    template_name = 'factory/parts/form.html'
    form_class = PartForm
    success_url = reverse_lazy('factory:part_list')


class PartDeleteView(ProtectedDeleteMixin, DeleteView):
    model = Part
    template_name = 'factory/parts/confirm_delete.html'
    success_url = reverse_lazy('factory:part_list')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'factory/employees/list.html'
    context_object_name = 'items'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'factory/employees/detail.html'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'factory/employees/form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('factory:employee_list')


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'factory/employees/form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('factory:employee_list')


class EmployeeDeleteView(ProtectedDeleteMixin, DeleteView):
    model = Employee
    template_name = 'factory/employees/confirm_delete.html'
    success_url = reverse_lazy('factory:employee_list')


class ProductionOrderListView(ListView):
    model = ProductionOrder
    template_name = 'factory/orders/list.html'
    context_object_name = 'items'


class ProductionOrderDetailView(DetailView):
    model = ProductionOrder
    template_name = 'factory/orders/detail.html'


class ProductionOrderCreateView(CreateView):
    model = ProductionOrder
    template_name = 'factory/orders/form.html'
    form_class = ProductionOrderForm
    success_url = reverse_lazy('factory:order_list')


class ProductionOrderUpdateView(UpdateView):
    model = ProductionOrder
    template_name = 'factory/orders/form.html'
    form_class = ProductionOrderForm
    success_url = reverse_lazy('factory:order_list')


class ProductionOrderDeleteView(ProtectedDeleteMixin, DeleteView):
    model = ProductionOrder
    template_name = 'factory/orders/confirm_delete.html'
    success_url = reverse_lazy('factory:order_list')


class QualityCheckListView(ListView):
    model = QualityCheck
    template_name = 'factory/quality/list.html'
    context_object_name = 'items'


class QualityCheckDetailView(DetailView):
    model = QualityCheck
    template_name = 'factory/quality/detail.html'


class QualityCheckCreateView(CreateView):
    model = QualityCheck
    template_name = 'factory/quality/form.html'
    form_class = QualityCheckForm
    success_url = reverse_lazy('factory:quality_list')


class QualityCheckUpdateView(UpdateView):
    model = QualityCheck
    template_name = 'factory/quality/form.html'
    form_class = QualityCheckForm
    success_url = reverse_lazy('factory:quality_list')


class QualityCheckDeleteView(ProtectedDeleteMixin, DeleteView):
    model = QualityCheck
    template_name = 'factory/quality/confirm_delete.html'
    success_url = reverse_lazy('factory:quality_list')
