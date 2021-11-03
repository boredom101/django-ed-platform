from django.db import models

class ItemInfo(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        abstract = True

class EducationLevel(ItemInfo):
    pass

class Grade(ItemInfo):
    level = models.ForeignKey(EducationLevel)

class Subject(ItemInfo):
    grades = models.ManyToManyField(Grade)

class Subtopic(ItemInfo):
    subjects = models.ManyToManyField(Subject)