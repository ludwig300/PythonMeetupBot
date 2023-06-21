from django.contrib import admin
from .models import User, Event, Report, Question


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'role')
    list_filter = ('role',)
    search_fields = ('username', 'firstname', 'lastname')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'datetime', 'event')
    list_filter = ('speaker', 'event')
    search_fields = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'report', 'created_at')
    list_filter = ('user', 'report')
    search_fields = ('question',)
