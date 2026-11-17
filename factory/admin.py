from django.contrib import admin

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

admin.site.register(VehicleCategory)
admin.site.register(Workshop)
admin.site.register(Supplier)
admin.site.register(Vehicle)
admin.site.register(Part)
admin.site.register(Employee)
admin.site.register(ProductionOrder)
admin.site.register(QualityCheck)
