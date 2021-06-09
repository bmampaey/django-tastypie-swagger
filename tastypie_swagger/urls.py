from .views import SwaggerView, ResourcesView, SchemaView
from tastypie_swagger.views import SwaggerSpecs2View

from django.urls import path

app_name = 'tastypie_swagger'
urlpatterns = [
    path('', SwaggerView.as_view(), name='index'),
    path('resources/', ResourcesView.as_view(), name='resources'),
    path('specs/swagger.json', SwaggerSpecs2View.as_view(), name='specs'),
    path('schema/<resource>/', SchemaView.as_view()),
    path('schema/', SchemaView.as_view(), name='schema'),
]
