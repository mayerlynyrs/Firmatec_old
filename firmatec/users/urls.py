"""Users urls."""

# Django
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views


urlpatterns = [
    # Management
    path(
        route='signin/',
        view=views.SignInView.as_view(),
        name='signin'
    ),
    path(
        route='logout/',
        view=auth_views.LogoutView.as_view(next_page='/users/signin/'),
        name='logout'
    ),
    path(
        route='',
        view=views.UserListView.as_view(),
        name='list'
     ),
    path(
        route='<int:planta_id>/',
        view=views.UserListView.as_view(),
        name='list'
    ),
    path(
        route='<int:user_id>/update/',
        view=views.update_user,
        name="update"
    ),
    path(
        route='create',
        view=views.create_user,
        name="create"
    ),
    path(
        route='<int:pk>/detail/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    path(
        route='change_password/',
        view=views.PasswordChangeView.as_view(),
        name='change_password'
    ),
    path(
        route='admin/<int:user_id>/change_password/',
        view=views.admin_change_password,
        name='admin_change_password'
    ),
    path(
        route='<int:user_id>/contrato/',
        view=views.generar_contrato_usuario,
        name='generar_contrato'
    )
]
