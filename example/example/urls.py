from django.urls import include, path
from django.contrib import admin
from demo.apis import api

urlpatterns = [
    path('api/', include(api.urls)),
    path('api/doc/', include('tastypie_swagger.urls', namespace='demo_api_swagger'),
      kwargs={
          'tastypie_api_module':'demo.apis.api',
          'namespace':'demo_api_swagger',
          'version': '0.1'}
    ),
    path('admin/', admin.site.urls),
]
