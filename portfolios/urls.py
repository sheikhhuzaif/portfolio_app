from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views
from django.contrib.auth import views as auth_views
app_name='portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.logoutUser, name='logout'),
    path('edit/', views.edit, name='edit'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('view/<str:username>/', views.display, name='view'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('settings/',views.settings,name='settings'),
    path('password/',views.password_change,name='password'),
    path('contact/',views.contact,name='contact')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
