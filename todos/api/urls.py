from django.urls import path, re_path

from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView
)

app_name = 'todos'

urlpatterns = [
    path('', TodoListView.as_view()),
    path('create/', TodoCreateView.as_view()),
    path('<pk>', TodoDetailView.as_view()),
    path('<pk>/update/', TodoUpdateView.as_view()),
    path('<pk>/delete/', TodoDeleteView.as_view())
]
