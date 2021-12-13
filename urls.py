from django.urls import path
# from .views import TodoViews
from . import views

urlpatterns = [
    # path('items/',TodoViews.as_view(),name="items"),
    # path('items/<int:id>/',TodoViews.as_view(),name="item")
    
    path('items/',views.getItems,name="items"),
    path('items/create/',views.createItem,name="create-item"),
    path('items/<int:id>/update/',views.updateItem,name="update-item"),
    path('items/<int:id>/delete/',views.deleteItem,name="delete-item"),
    path('items/<int:id>/',views.getItem,name="item"),
]

