from django.contrib import admin
from .models import *

admin.site.register(Questions)
admin.site.register(AnswersOfParticipant)

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'status')
    list_display_links = ('id', 'question',)


@admin.register(Quizs)
class QuizsAdmin(admin.ModelAdmin):
    list_display = ('id', 'participant', 'quantity', 'true', 'false', 'percentage', 'is_finished', 'date')
    list_display_links = ('id', 'participant',)
    list_filter = ('is_finished',)
    date_hierarchy = 'date'