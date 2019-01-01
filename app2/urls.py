from django.urls import path
from .views import person_list, person_lista, person_new, update_person, delete_person

urlpatterns = [
    path('list/', person_lista, name = "person_lista"),
    path('', person_list),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>', update_person, name='update_person'),
    path('delete/<int:id>', delete_person, name='delete_person'),

]
