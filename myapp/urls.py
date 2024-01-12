from django.urls import path
from .views import Home, post_ditile
app_name='myapp'
urlpatterns=[
    path('',Home, name='home'),
    path('post-ditile/<str:year>/<str:month>/<str:day>/<str:slug>/',post_ditile, name='postditile'),
]