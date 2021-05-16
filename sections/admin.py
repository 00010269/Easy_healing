from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin

from .models import Pharmacy, Medicine, Distribution

@admin.register(Pharmacy)
class PharmacyAdmin(ImportExportActionModelAdmin):
    search_fields = ("name", "location", )
    list_display = ("name", "location", "phone_number", )



@admin.register(Medicine)
class MedicineAdmin(ImportExportActionModelAdmin):
    search_fields = ("name", "shape", "text")
    list_display = ("name", "shape", "text", )
    list_filter = ("shape",)



@admin.register(Distribution)
class DistributionAdmin(ImportExportActionModelAdmin):
    list_display = ("medicine", "pharmacy", "price", "quantity")
    autocomplete_fields = ("medicine", "pharmacy", )
    list_select_related = ("medicine", "pharmacy")






