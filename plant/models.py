from django.db import models

# Create your models here.
# Бригада
class Brigade(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='brigade_leader')
    def __str__(self):
        return self.name
# Сотрудник
class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name='brigade_employees')
    def __str__(self):
        return self.name
# Оборудование
class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
# Ремонт
class Repair(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='repairs')
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name='brigade_repairs')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255)
# Задача
class Task(models.Model):
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, related_name='repair_tasks')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_tasks')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255)