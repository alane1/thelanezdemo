from django.db import models

class Student(models.Model):
    name = models.TextField()
    address = models.TextField()
    phoneNumber = models.TextField()
    emailAddress = models.TextField()
    studentNumber = models.TextField()
    averageMark = models.TextField()

class Professor(models.Model):
    name = models.TextField()
    address = models.TextField()
    phoneNumber = models.TextField()
    emailAddress = models.TextField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)

class Seminar(models.Model):
    name = models.TextField()
    seminarNumber = models.TextField()
    fees = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    professor = models.ForeignKey(Professor, blank=True, null=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student)
    seminar = models.ForeignKey(Seminar)
    marksRecieved = models.TextField()

class Waitlist(models.Model):
    student = models.ForeignKey(Student)
    seminar = models.ForeignKey(Seminar)

class Note(models.Model):
    name = models.TextField()
    content = models.TextField()
    email = models.EmailField()
    # dateTime = models.DateTimeField() ### need to fix validation to convert datetimepicker output into datetime objects
    ### when change it back add this to where its printed out in the html  .strftime('%m/%d/%Y %H:%M:%S')
    dateTime = models.TextField()

class GalleryImage(models.Model):
    filename = models.TextField()
    title = models.TextField()
