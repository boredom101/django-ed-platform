from django.shortcuts import render
from django.views import generic

from . import models

class GradeListView(generic.ListView):
    model = models.Grade

class SubjectListView(generic.ListView):
    model = models.Subject

class SubtopicListView(generic.ListView):
    model = models.Subtopic

class SubjectDetailView(generic.DetailView):
    model = models.Subject

class SubtopicDetailView(generic.DetailView):
    model = models.Subtopic

class SubjectCreateView(generic.CreateView):
    model = models.Subject

class SubtopicCreateView(generic.CreateView):
    model = models.Subtopic