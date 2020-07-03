from django.urls import path
from myapp import views 

urlpatterns = [
    path('',views.home),
    path('tag/<str:tag_slug>',views.home,name='post_list_by_tag_name'),
    path('read/<int:pk>',views.post_detail,name='post_detail'),
    path('<int:id>/share/',views.Email_send_view)

]
