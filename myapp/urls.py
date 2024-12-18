from django.urls import path
from.import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('add/',views.Create,name='create'),
    path('Dele/<int:id>',views.Dele,name='delete'),
    path('History/',views.History,name='history'),
    path('Update/<int:id>',views.Update,name='update'),
    path('restore/<int:id>',views.restore,name='restore'),
    path('dele_restore/<int:id>',views.del_restore,name='dele_restore'),
    path('restoreall/',views.restoreall,name='restoreall'),
    path('deleteall/',views.deleteall,name='deleteall'),
    path('about/',views.about,name='about'),
    
]