from rest_framework import routers
# from .views import NoteList,NoteDetail
from .views import NotesModelViewSet
from django.urls import path,include
routers=routers.DefaultRouter()
# routers.register(r'Notes-list',NoteList)
# routers.register(r'Notes-details',NoteDetail)
routers.register(r'notes',NotesModelViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]

# from django.urls import path
# from api import views
# urlpatterns = [
#     path('', views.NoteList.as_view()),
#     path('<int:pk>/', views.NoteDetail.as_view()),
# ]