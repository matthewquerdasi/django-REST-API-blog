from django.urls import path
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    # displays index.html template
    path('', TemplateView.as_view(template_name="blog/index.html")),
]
