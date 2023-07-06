from django.contrib import admin
from attendence.models import Attendence,Class_name,date_wise
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    model=CustomUser
    list_display=['pk','email','username','staff_id']
    add_fieldsets=UserAdmin.add_fieldsets + ((None,{'fields':('email','first_name','last_name','staff_id')}),
    )
    fieldsets=UserAdmin.fieldsets+ ((None,{'fields':('staff_id','pincode')}),
    )
admin.site.register(CustomUser,CustomUserAdmin)

admin.site.register(Attendence)
admin.site.register(Class_name)
admin.site.register(date_wise)
# Register your models here.
