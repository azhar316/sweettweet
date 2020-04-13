from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserProfile
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):

    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('username', 'is_superuser', 'is_staff', 'is_active', )
    list_filter = ('username', 'is_superuser', 'is_staff', 'is_active', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'email',)
    ordering = ('date_joined',)


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
