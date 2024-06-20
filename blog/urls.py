from django.urls import path
from .views import TemplateView

app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
]

print("Barbie")