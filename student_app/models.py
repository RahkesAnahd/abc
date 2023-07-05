from django.db import models

class students_data(models.Model):
    Roll_Number = models.IntegerField()
    Student_Name= models.CharField(max_length=255)
    Date_of_Birth= models.DateField()

class students_marks(models.Model):
    details = models.ForeignKey(students_data,on_delete=models.CASCADE)
    English = models.IntegerField(range(0,100))
    Science = models.IntegerField(range(0, 100))
    Maths = models.IntegerField(range(0, 100))
    social = models.IntegerField(range(0, 100))


