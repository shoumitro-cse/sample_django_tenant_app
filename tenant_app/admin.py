from django.contrib import admin
from django.apps import apps
from django_tenants.utils import get_public_schema_name


class TenantsAdmin(admin.ModelAdmin):
    # https://stackoverflow.com/questions/60521498/hide-public-model-from-tenant-admin-in-django

    # Hides tenants models from public
    @staticmethod
    def has_tenant(request):
        # public schema don't have any tenant
        if hasattr(request, "tenant"):
            return True
        else:
            return False

    def has_view_permission(self, request, view=None):
        # print(get_public_schema_name())
        return self.has_tenant(request)

        # print(request.tenant.schema_name, "--", get_public_schema_name())
        # if request.tenant.schema_name == get_public_schema_name():
        #     return True
        # else:
        #     return False

    def has_add_permission(self, request, view=None):
        try:
            if request.tenant.schema_name == get_public_schema_name():
                return True
            else:
                return False
        except Exception as e:
            return False

    def has_change_permission(self, request, view=None):
        try:
            if request.tenant.schema_name == get_public_schema_name():
                return True
            else:
                return False
        except Exception as e:
            return False

    def has_delete_permission(self, request, view=None):
        try:
            if request.tenant.schema_name == get_public_schema_name():
                return True
            else:
                return False
        except Exception as e:
            return False

    def has_view_or_change_permission(self, request, view=None):
        try:
            if request.tenant.schema_name == get_public_schema_name():
                return True
            else:
                return False
        except Exception as e:
            return False


app = apps.get_app_config('tenant_app')
for model_name, model in app.models.items():
    admin.site.register(model, TenantsAdmin)
