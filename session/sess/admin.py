from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import *

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    fields = ('title', 'text')
