from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import products, categories

admin.site.register(categories)
admin.site.register(products)

##@admin.register(products)
##class ViewAdmin(ImportExportModelAdmin):
   ## pass