# Maps URLs (web addresses) to views. For instance, it connects `/login` to a view function that shows the login page.
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), # views.home call the def home function in views.py
    path('logout/', views.user_logout, name='logout'), # views.user_logout call the def user_logout function in views.py
    path('details/<int:pk>', views.user_details, name='details'), # views.user_details call the def user_details function in views.py
    path('delete/<int:pk>', views.user_delete, name='delete'), # views.user_delete call the def user_delete function in views.py
    path('add/', views.add_record, name='add'),
    path('update/<int:pk>', views.user_update, name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to sereve media files during development
