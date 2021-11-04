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
    level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)

class Subject(ItemInfo):
    grades = models.ManyToManyField(Grade)

class Subtopic(ItemInfo):
    subjects = models.ManyToManyField(Subject)
    def get_grades(self):
        return Grade.objects.filter(subject__subtopic=self).distinct().order_by('id')
