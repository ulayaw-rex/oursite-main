from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_login),
    path('login', views.login_view, name='login'),
    path('genders', views.index_gender),
    path('gender/create', views.create_gender),
    path('genders_store', views.store_gender),
    path('gender/show/<int:gender_id>',views.show_gender),
    path('gender/edit/<int:gender_id>', views.edit_gender),
    path('gender/update/<int:gender_id>', views.update_gender),
    path('gender/delete/<int:gender_id>', views.delete_gender),
    path('gender/destroy/<int:gender_id>', views.destroy_gender),
    path('user', views.index_user, name='user'),
    path('user/create', views.create_user),
    path('user/store', views.store_user),
    path('user/show/<int:student_id>', views.show_user),
    path('user/delete/<int:student_id>', views.delete_user),
    path('user/destroy/<int:student_id>', views.destroy_user),
    path('user/edit/<int:student_id>', views.edit_user),
    path('user/update/<int:student_id>', views.update_user),
    path('teacher/create', views.create_sign_up),
    path('teacher/store', views.store_sign_up),
]
