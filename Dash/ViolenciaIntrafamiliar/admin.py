from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from . import models


class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id',)

class violenciaAdmin(admin.ModelAdmin):
    list_display = ('Departamento', 'Municipio', 'CodigoDane', 'ArmasMedios', 'FechaHecho','Genero','GrupoEtario','Cantidad')
    list_filter = ('FechaHecho','Departamento')
    search_fields = ('Departamento', ) 


admin.site.register(models.violencia, violenciaAdmin,)