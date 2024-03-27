from django.urls import path
from .views import *


urlpatterns = [
    path("cratestudent/", Creatingstudent.as_view(), name="creaingstudent"),
    path("classbaslist/<str:name>/", ListClassBase.as_view(), name="list_with_name"),
    path("listall/", List_all.as_view(), name="all"),
    path("namebaselist/<str:name>/", Namebasesearch.as_view(), name="list_with_name"),
    path("addteacher/", Addingteacher.as_view(), name="addteacher"),
    path("createsubject/", Subjectcreate.as_view(), name="createsubject"),
    path("subjectall/", Subjectall.as_view(), name="createsubject"),
]
