from django.urls import path

from MonitorService.view import monitor_view

urlpatterns = [
    path('monitor_info/', monitor_view.MonitorInfo.as_view(),name="MonitorInfo"),
]
