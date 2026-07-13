from django.db import models
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=60)
    qualification = models.CharField(max_length=60)
    contact = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    standard = models.IntegerField()
    roll_number = models.IntegerField()
    contact = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)