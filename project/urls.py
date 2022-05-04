from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from project import views

urlpatterns = [
    path('project/', views.ProjectList.as_view()),
    path('project/<int:pk>/', views.ProjectDetail.as_view()),
    path('deliverable/', views.DeliverableList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
