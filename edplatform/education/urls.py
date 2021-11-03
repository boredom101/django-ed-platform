from django.urls import path

from . import views

urlpatterns = [
    path('grades/list/', views.GradeListView.as_view(), name='grades'),
    path('subjects/list/', views.SubjectListView.as_view(), name='subjects'),
    path('subjects/create/', views.SubjectCreateView.as_view(), name='subject-create'),
    path('subjects/<int:pk>', views.SubjectDetailView.as_view(), name='subject-detail'),
    path('subtopics/list/', views.SubtopicListView.as_view(), name='subtopics'),
    path('subtopics/create/', views.SubtopicCreateView.as_view(), name='subtopic-create'),
    path('subtopics/<int:pk>', views.SubtopicDetailView.as_view(), name='subtopic-detail'),
]