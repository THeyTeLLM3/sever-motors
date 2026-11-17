from django import forms

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


class VehicleCategoryForm(forms.ModelForm):
    class Meta:
        model = VehicleCategory
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['name', 'building', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'city']


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'category', 'description', 'price', 'power', 'photo', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'article', 'supplier', 'description', 'price', 'stock', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'workshop', 'hired_on']
        widgets = {
            'hired_on': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class ProductionOrderForm(forms.ModelForm):
    class Meta:
        model = ProductionOrder
        fields = ['number', 'vehicle', 'workshop', 'quantity', 'planned_on', 'status']
        widgets = {
            'planned_on': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class QualityCheckForm(forms.ModelForm):
    class Meta:
        model = QualityCheck
        fields = ['order', 'inspector', 'checked_on', 'passed', 'notes']
        widgets = {
            'checked_on': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
