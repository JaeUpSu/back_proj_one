from django.contrib import admin
from .models import Review

# Register your models here.
# admin.site.register(User)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user","content","like","reply",)
    search_fields=("user", "content", )

  