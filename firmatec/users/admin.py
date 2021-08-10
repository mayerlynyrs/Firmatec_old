"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Utilities
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Models
from users.models import User, Sexo, Civil, Nacionalidades, SistemaSalud, SistemaPrevision, Banco, TipoCta
# sexo, estado_civil, fecha_nac, telefono, nacionalidades, domicilio,
# planta, sistema_salud, sistema_prevision, banco, tipo_cta, cuenta


class SexoSetResource(resources.ModelResource):

    class Meta:
        model = Sexo
        fields = ('id', 'nombre', 'status', )


class CivilSetResource(resources.ModelResource):

    class Meta:
        model = Civil
        fields = ('id', 'nombre', 'status', )


class NacionalidadesSetResource(resources.ModelResource):

    class Meta:
        model = Nacionalidades
        fields = ('id', 'nombre', 'status', )


class SistemaSaludSetResource(resources.ModelResource):

    class Meta:
        model = SistemaSalud
        fields = ('id', 'nombre', 'status', )


class SistemaPrevisionSetResource(resources.ModelResource):

    class Meta:
        model = SistemaPrevision
        fields = ('id', 'nombre', 'status', )


class BancoSetResource(resources.ModelResource):

    class Meta:
        model = Banco
        fields = ('id', 'nombre', 'status', )


class TipoCtaSetResource(resources.ModelResource):

    class Meta:
        model = TipoCta
        fields = ('id', 'nombre', 'status', )


class UserSetResource(resources.ModelResource):

    class Meta:
        model = User
        fields = ['id', 'rut', 'first_name', 'last_name', 'codigo', 'username', 'email', 'telefono',
                  'is_active', 'cambiar_clave', 'created_at', 'created', 'modified_at', 'modified', ]


@admin.register(Sexo)
class SexoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """SexoAdmin model admin."""

    resource_class = SexoSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


@admin.register(Civil)
class CivilAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """CivilAdmin model admin."""

    resource_class = CivilSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


@admin.register(Nacionalidades)
class NacionalidadesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """NacionalidadesAdmin model admin."""

    resource_class = NacionalidadesSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


@admin.register(SistemaSalud)
class SistemaSaludAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """SistemaSaludAdmin model admin."""

    resource_class = SistemaSaludSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


@admin.register(SistemaPrevision)
class SistemaPrevisionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """SistemaPrevisionAdmin model admin."""

    resource_class = SistemaPrevisionSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


@admin.register(Banco)
class BancoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """BancoAdmin model admin."""

    resource_class = BancoSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


@admin.register(TipoCta)
class TipoCtaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """TipoCtaAdmin model admin."""

    resource_class = TipoCtaSetResource
    fields = ('nombre', )
    list_display = ('id', 'nombre',)
    search_fields = ['nombre', ]


class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    """User model admin."""

    resource_class = UserSetResource
    fieldsets = UserAdmin.fieldsets + (
        ('Más Información', {
            'fields': ('codigo', 'rut', 'sexo', 'estado_civil', 'fecha_nac', 'telefono', 'nacionalidades',
                       'domicilio', 'planta', 'sistema_salud', 'sistema_prevision', 'banco', 'tipo_cta',
                       'cuenta', 'cambiar_clave', 'atributos', )
        }),
    )
    list_display = ('rut', 'first_name', 'last_name', 'email', 'codigo', 'is_active')
    list_filter = ('planta', 'is_staff', 'created', 'modified')
    search_fields = ('first_name', 'last_name', 'rut', 'planta__nombre')


admin.site.register(User, CustomUserAdmin)
