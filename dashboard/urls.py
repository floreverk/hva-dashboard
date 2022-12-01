from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
    path('collection', views.collectiondash),
    path('bugs', views.bugsdash),
    path('studio', views.studiodash),
    path('thesauri', views.thesauridash),
    path('rschijf', views.rschijfdash),
    path('registrationquality', views.registrationquality),
    path('rightsquality', views.rightsquality),
    path('thesauriquality', views.thesauriquality),
    path('rschijfquality', views.rschijfquality),
    path('registrationmanual', views.registrationmanual),
    path('rightsmanual', views.rightsmanual),
    path('faq', views.faq),
    path('thesauruscheck', views.thesauruscheck),
    path('studiodatabase', views.studiodatabase, name='studio'),
    path('bugsdatabase', views.bugsdatabase, name='bugs'),
    path('rschijftool', views.rschijftool),
    path('assotool', views.assotool)
]
