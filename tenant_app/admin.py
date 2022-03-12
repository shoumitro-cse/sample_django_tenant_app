from django.contrib import admin
from django.apps import apps
from django_tenants.utils import get_public_schema_name


# tenant app hide from public
class TenantsAdmin(admin.ModelAdmin):
    # https://stackoverflow.com/questions/60521498/hide-public-model-from-tenant-admin-in-django

    @staticmethod
    def has_tenant(request):
        # public schema don't have any tenant
        if hasattr(request, "tenant"):
            return True
        else:
            return False

    def has_view_permission(self, request, view=None):
        if self.has_tenant(request):
            # print('current schema name: ', request.tenant.schema_name)
            # print('public schema name: ', get_public_schema_name())
            if request.tenant.schema_name == get_public_schema_name():
                return False
            else:
                return True

    def has_add_permission(self, request, view=None):
        if self.has_tenant(request):
            if request.tenant.schema_name == get_public_schema_name():
                return False
            else:
                return True

    def has_change_permission(self, request, view=None):
        if self.has_tenant(request):
            if request.tenant.schema_name == get_public_schema_name():
                return False
            else:
                return True

    def has_delete_permission(self, request, view=None):
        if self.has_tenant(request):
            if request.tenant.schema_name == get_public_schema_name():
                return False
            else:
                return True

    def has_view_or_change_permission(self, request, view=None):
        if self.has_tenant(request):
            if request.tenant.schema_name == get_public_schema_name():
                return False
            else:
                return True


app = apps.get_app_config('tenant_app')
for model_name, model in app.models.items():
    admin.site.register(model, TenantsAdmin)
