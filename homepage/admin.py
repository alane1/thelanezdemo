from django.db import models
from django.contrib import admin
from .models import *

# register any models here
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Seminar)
admin.site.register(Enrollment)
admin.site.register(Waitlist)
