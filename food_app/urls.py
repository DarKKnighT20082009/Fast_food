from django.urls import path
from .views import main_page, menu_page, about_page, book_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('menu/', menu_page, name='menu_page'),
    path('about/', about_page, name='about_page'),
    path('/', book_page, name='book_page'),


]
