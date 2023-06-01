from django.urls import path


from .views import CurrentDateView, RandomNumberView, HelloWorldView, IndexView


urlpatterns = [
   path('', IndexView.as_view()),
   path('datetime/', CurrentDateView.as_view()),
   path('random/', RandomNumberView.as_view()),
   path('hello/', HelloWorldView.as_view()),
]
