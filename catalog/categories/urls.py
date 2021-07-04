from catalog.categories.views import category_delete, category_edit, category_new
from django.urls import path
app_name='category'
urlpatterns = [
    path('new', category_new, name="new"),
    path('<int:id>', category_delete, name="delete"),
    path('<int:id>', category_edit, name="edit"),
]
