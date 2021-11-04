from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse

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
    fields = '__all__'

class SubtopicCreateView(generic.CreateView):
    model = models.Subtopic
    fields = '__all__'

def jsonView(request):
    data = []
    for level in models.EducationLevel.objects.all():
        classes = []
        for grade in models.Grade.objects.filter(level=level):
            topics = []
            for subject in models.Subject.objects.filter(grades=grade):
                subtopics = []
                for subtopic in models.Subtopic.objects.filter(subjects=subject):
                    topics.append({
                        'id': subtopic.id,
                        'label': subtopic.name
                    })
                topics.append({
                    'id': subject.id,
                    'label': subject.name,
                    'mainSubjects': subtopics
                })
            classes.append({
                'id': grade.id,
                'label': grade.name,
                'topics': topics
            })
        data.append({
            'id': level.id,
            'label': level.name,
            'classes': classes
        })
    return JsonResponse({'code': 0, 'data': data})