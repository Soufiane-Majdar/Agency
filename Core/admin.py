from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'company_name')
    search_fields = ('name', 'email', 'phone_number', 'company_name')
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'client', 'plan', 'status')
    search_fields = ('title', 'start_date', 'end_date', 'client', 'plan', 'status')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client', 'content','rating')
    search_fields = ('client', 'content','rating')




@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject', 'message')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','date','is_subscribed')
    search_fields = ('email','date')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','category')
    search_fields = ('title','category')


admin.site.register(SMTPHost)
admin.site.register(WebInfo)
admin.site.register(Item)