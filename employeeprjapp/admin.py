from django.contrib import admin

from django.contrib import admin
from .models import Name, Designation, Salary, Employee

# Register your models here.
class MasterAdmin(admin.ModelAdmin):
    # in order to exclude the field 'created_user' from the form
    exclude = ['created_user']

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    # To order Active field last in all forms
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj=obj)
        try:
            fields.remove('isactive') # type: ignore
        except ValueError:
            pass  # 'isactive' not in fields, so no need to remove it
        return fields 

    # To save the logged in user id to the table when a record is added.
    # https://stackoverflow.com/questions/6760602/how-can-i-get-current-logged-user-id-in-django-admin-panel
    def save_model(self, request, obj, form, change):
        obj.created_user = request.user
        super().save_model(request, obj, form, change)

class TransactionAdmin(admin.ModelAdmin):

    # in order to exclude the field 'created_user' from the form
    exclude = ['created_user']
    
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

class NameAdmin(MasterAdmin):
    list_display = ['name']

class DesignationAdmin(MasterAdmin):
    list_display = ['designation']

class SalaryAdmin(MasterAdmin):
    list_display = ['salary']

class EmployeeAdmin(MasterAdmin):
    list_display = ['name', 'designation', 'salary']

    # Remove any many-to-many fields or reverse foreign keys from list_display
    # Ensure 'isactive' is a valid attribute or method of the Employee model

admin.site.register(Name, NameAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(Employee, EmployeeAdmin)
