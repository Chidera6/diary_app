from django.urls import path
from .import views

app_name = 'dia'

urlpatterns = [
    path('index/<int:id>/',views.index,name='index'),
    path("edit/<int:id>/",views.edit,name='edits'),
    path("create/",views.add_diary,name='add'),
    path("delete/<int:id>/",views.delete,name='delete'),
    path('',views.home,name='home'),
    path("see-category",views.see_category,name='see-category'),
    path("show-category/<int:id>/",views.show_category,name='show-category'),
    path("edit-category/<int:id>/",views.edit_category,name='edit-category'),
    path("create-category/",views.add_category,name='add-category'),
    path("delete-category/<int:id>/",views.delete_category,name='delete-category'),
    path("register/",views.register_request,name='register'),
    path("content/<int:id>/",views.show,name='show'),
    path("login/",views.login_request,name='login'),
    path("logout/",views.logout_request,name='logout')
]