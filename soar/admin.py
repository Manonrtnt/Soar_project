from django.contrib import admin

from .models import CaptureRequest

# class RequestCode(admin.TabularInline):
#     model = RequestCode
#     extra = 2

# class CaptureRequest(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["Request name"]}),
#         (None, {"fields": ["Request user"]}),
#         ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
#     ]
#     # inlines = [RequestCode]
#     # list_display = ["question_text", "pub_date", "was_published_recently"]
#     # list_filter = ["pub_date"]
#     # search_fields = ["question_text"]

class CaptureRequestAdmin(admin.ModelAdmin):
    list_display = ['requestName', 'requestUser', 'requestDate', 'requestCode']

# admin.site.register(CaptureRequest)

admin.site.register(CaptureRequest, CaptureRequestAdmin)