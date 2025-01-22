from django.contrib import admin
from .models import (
    CustomUser,
    Citizen,
    City,
    Street,
    CityService,
    Employee,
    Category,
    Appeal,
    Status,
    AppealProcess,
    Message
)
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'surname', 'name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('surname', 'name', 'patronymic', 'phone_number'),
        }),
    )


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'street', 'house', 'flat')
    search_fields = ('user__username', 'city__name', 'street__name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_city')
    search_fields = ('name_city',)


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_street', 'city')
    search_fields = ('name_street',)
    list_filter = ('city',)


@admin.register(CityService)
class CityServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'street', 'house', 'flat', 'tel')
    search_fields = ('name', 'tel')
    list_filter = ('city',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'service')
    search_fields = ('user__username', 'service__name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_official', 'name_short')
    search_fields = ('name_official', 'name_short')


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'citizen', 'category', 'date_time', 'employee', 'description_problem')
    search_fields = ('description_problem',)
    list_filter = ('category', 'date_time')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_status')
    search_fields = ('name_status',)


@admin.register(AppealProcess)
class AppealProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'appeal', 'status', 'date_time_setting_status')
    list_filter = ('status', 'date_time_setting_status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'appeal', 'employee', 'citizen', 'message', 'date_time')
    search_fields = ('message',)
    list_filter = ('date_time',)
