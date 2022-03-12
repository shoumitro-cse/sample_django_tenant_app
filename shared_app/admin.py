from django.contrib import admin
from django.apps import apps
from django_tenants.utils import get_public_schema_name


# Shared app read only for tenant
class SharedAdmin(admin.ModelAdmin):

    @staticmethod
    def has_tenant(request):
        # print('current schema name: ', request.tenant.schema_name)
        # print('public schema name: ', get_public_schema_name())

        # public schema don't have any tenant
        if hasattr(request, "tenant"):
            return True
        else:
            return False

    def has_view_permission(self, request, view=None):
        return True

        # if self.has_tenant(request):
        #     # print('current schema name: ', request.tenant.schema_name)
        #     # print('public schema name: ', get_public_schema_name())
        #     if request.tenant.schema_name != get_public_schema_name():
        #         return False

    def has_add_permission(self, request, view=None):
        if self.has_tenant(request):
            if request.tenant.schema_name != get_public_schema_name():
                return False
        return True

    def has_change_permission(self, request, view=None):
        if self.has_tenant(request):
            if request.tenant.schema_name != get_public_schema_name():
                return False
        return True

    def has_delete_permission(self, request, view=None):
        if self.has_tenant(request):
            if request.tenant.schema_name != get_public_schema_name():
                return False
        return True

    # def has_view_or_change_permission(self, request, view=None):
    #     if self.has_tenant(request):
    #         if request.tenant.schema_name != get_public_schema_name():
    #             return False
    #     return True


depot_app_config = apps.get_app_config('shared_app')
for model in depot_app_config.get_models():
    admin.site.register(model, SharedAdmin)
