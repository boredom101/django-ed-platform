from django.db import models
from django.urls import reverse

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
    def get_absolute_url(self):
        return reverse('subject-detail', args=[str(self.pk)])

class Subtopic(ItemInfo):
    subjects = models.ManyToManyField(Subject)
    def get_grades(self):
        return Grade.objects.filter(subject__subtopic=self).distinct().order_by('id')
    def get_absolute_url(self):
        return reverse('subtopic-detail', args=[str(self.pk)])