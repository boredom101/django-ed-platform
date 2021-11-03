from django.contrib import admin

from . import models

admin.site.register(models.EducationLevel)
admin.site.register(models.Grade)
admin.site.register(models.Subject)
admin.site.register(models.Subtopic)