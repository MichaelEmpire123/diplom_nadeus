from django.db import models
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    name_city = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name_city


class Street(models.Model):
    name_street = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='streets')

    def __str__(self):
        return self.name_street


class CustomUser(AbstractUser):
    surname = models.CharField(max_length=255, verbose_name='Фамилия', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    patronymic = models.CharField(max_length=255, verbose_name='Отчество', blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон', unique=True)

    def __str__(self):
        return self.username


class Citizen(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='citizen')
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    street = models.ForeignKey('Street', on_delete=models.CASCADE)
    house = models.CharField(max_length=255)
    flat = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Житель {self.user.surname} {self.user.name}"


class CityService(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    street = models.ForeignKey('Street', on_delete=models.CASCADE)
    house = models.CharField(max_length=100)
    flat = models.IntegerField(null=True, blank=True)
    tel = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee')
    service = models.ForeignKey('CityService', on_delete=models.CASCADE)

    def __str__(self):
        return f"Сотрудник {self.user.surname} {self.user.name}"


class Category(models.Model):
    name_official = models.CharField(max_length=255)
    name_short = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name_official


class Appeal(models.Model):
    citizen = models.ForeignKey('Citizen', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description_problem = models.TextField()
    photo = models.ImageField(upload_to='appeals_photos/', null=True, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Appeal #{self.id} by {self.citizen.user.name}"


class Status(models.Model):
    name_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name_status


class AppealProcess(models.Model):
    appeal = models.ForeignKey('Appeal', on_delete=models.CASCADE, related_name='processes')
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    date_time_setting_status = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='process_photos/', null=True, blank=True)

    def __str__(self):
        return f"Process #{self.id} for Appeal #{self.appeal.id}"


class Message(models.Model):
    appeal = models.ForeignKey('Appeal', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)
    citizen = models.ForeignKey('Citizen', on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message #{self.id} for Appeal #{self.appeal.id}"
