from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        ("Profile", {
                "fields": ("email", "password", "is_business"),
                "classes": ("wide",),
            },
        ),
        ("Permissions",{
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
                # 접었다 폈다 하는기능
                "classes": ("collapse",),
            },
        ),
        ("Important Dates", {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = ("username", "email", "name", "is_business")
    # fieldsets = None
    # fields = ("username", "name", "email", "password" , )
    # list_display = ("username", "name","email",)
    # list_display = ("nickname","phone","is_business","gender","profileIntroduce")
    # list_filter=("is_business",)
    search_fields=("name",)