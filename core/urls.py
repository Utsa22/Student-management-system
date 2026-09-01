from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),

    path(
        'register/',
        views.RegisterView.as_view(),
        name='register'
    ),

    path(
        'login/',
        views.UserLoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        views.UserLogoutView.as_view(),
        name='logout'
    ),

    path(
        'students/',
        views.StudentListView.as_view(),
        name='student_list'
    ),

    path(
        'students/add/',
        views.StudentCreateView.as_view(),
        name='student_add'
    ),

    path(
        'students/<int:pk>/',
        views.StudentDetailView.as_view(),
        name='student_detail'
    ),

    path(
        'students/<int:pk>/edit/',
        views.StudentUpdateView.as_view(),
        name='student_update'
    ),

    path(
        'students/<int:pk>/delete/',
        views.StudentDeleteView.as_view(),
        name='student_delete'
    ),
]