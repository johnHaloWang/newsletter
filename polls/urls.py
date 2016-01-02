from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view()),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view()),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote),
]