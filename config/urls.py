"""Main URLs module."""

from django.conf import settings
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from utils import views

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('', views.Home.as_view(), name='home'),

    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('ficheros/', include(('ficheros.urls', 'ficheros'), namespace='ficheros')),
    path('contratos/', include(('contratos.urls', 'contratos'), namespace='contratos')),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        html_email_template_name='registration/password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

