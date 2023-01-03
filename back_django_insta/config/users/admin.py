from django.contrib import admin
from .models import User

# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("nickname","phone","is_business","gender","profileIntroduce")
    list_filter=("is_business",)
    search_fields=("nickname", "phone", )