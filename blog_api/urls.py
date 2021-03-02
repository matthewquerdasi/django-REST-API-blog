from django.urls import path
from .views import PostList, PostDetail


app_name = 'blog_api'

# API endpoints
urlpatterns = [
    # endpoint for PostDetail view 
    path('<int:pl>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
]
