from django.contrib import admin
from django.utils.html import format_html
from .models import Feed

# Register your models here.
# admin.site.register(User)

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ("user","content","image_tag","like","create_at", "update_at",)
    search_fields=("content", "user", )

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50px;"/>'.format("https://www.infostockdaily.co.kr/news/photo/202210/181980_156509_1944.jpg"))
    
    image_tag.short_description = "img"