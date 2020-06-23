from django.urls import path, include
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/', views.jobs_index, name='index'),
    path('jobs/<int:job_id>/', views.jobs_detail, name='detail'),
    path('jobs/jobs_create/', views.JobCreate.as_view(), name='jobs_create'),
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
    path('jobs/<int:job_id>/add_note/', views.add_note, name='add_note'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
