from django.contrib import admin
from .models import Review

# Register your models here.
# admin.site.register(User)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user","content","like","reply","create_at", "update_at",)
    search_fields=("user", "content", )

  