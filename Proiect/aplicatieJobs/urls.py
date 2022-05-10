from django.urls import path

from aplicatieJobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JobsView.as_view(), name='lista_jobs'),
    path('adaugare/', views.CreateJobsView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateJobsView.as_view(), name='modifica'),
    path('<int:pk>/stergere/', views.delete_jobs, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_jobs, name='activeaza'),]