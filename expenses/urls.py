from django.urls import path
from . import views

urlpatterns=[
    path('api/create_expense/',views.create_expense_api,name="create_expense_api"),
    path('api/list_expense/',views.list_expense_api,name="list_expense_api"),
    path('api/detail_expense/<int:id>/',views.detail_expense_api,name="detail_expense_api"),
    path('api/update_expense/<int:id>/',views.update_expense_api,name="update_expense_api"),
    path('api/delete_expense/<int:id>/',views.delete_expense_api,name="delete_expense_api"),
]