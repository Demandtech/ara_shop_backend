from django.contrib import admin
from .models import NewsLetter

# Register your models here.
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

admin.site.register(NewsLetter, NewsLetterAdmin)