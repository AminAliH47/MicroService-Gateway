from django.urls import path
from crud import views

app_name = "crud"

urlpatterns = (
    path('', views.UsersList.as_view(), name="list"),
    path('<int:pk>/', views.RetrieveUser.as_view(), name="retrieve"),
    path('create/', views.CreateUser.as_view(), name="create"),
    path('update/<int:pk>/', views.UpdateUser.as_view(), name="update"),
    path('delete/<int:pk>/', views.DeleteUser.as_view(), name="delete"),
)
