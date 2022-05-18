from django.db import models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

class Student(models.Model):
    name = models.CharField(max_length=80)
    up = models.IntegerField(unique=True)

class Buddy(models.Model):
    class Meta:
        unique_together = (('student', 'buddy', 'subject'),)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    buddy = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='buddy')
    subject = models.TextField()
    priority = models.IntegerField()

class InitialSchedule(models.Model):
    subject = models.TextField()
    class_no = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class FinalSchedule(models.Model):
    subject = models.TextField()
    class_no = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Preference(models.Model):
    subject = models.TextField()
    class_no = models.IntegerField()
    priority = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class GiveIn(models.Model):
    subject = models.TextField()
    class_no = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 

class Deadline(models.Model):
    time = models.DateTimeField()

    def validate_unique(self, exclude=None):
        if Deadline.objects.count() != 0:
            raise ValidationError({NON_FIELD_ERRORS: ["There can be only one!"]})