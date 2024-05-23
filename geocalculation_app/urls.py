
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='index_view'),
    path('download-processed-csv/', views.download_processed_csv, name='download_processed_csv'),
    
]
