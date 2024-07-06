from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('login/loguser/', views.loguser, name='loguser'),
	path('signup/adduser/', views.adduser, name='adduser'),
  path('user/', views.user, name='user'),
  path('user/add/', views.add, name='add'),
  path('user/update/<int:id>', views.update, name='update'),
  path('user/update/updatetodo/<int:id>', views.updatetodo, name='updatetodo'),
  path('user/add/addtodo/', views.addtodo, name='addtodo'),
  path('user/deletedata/<int:id>', views.deletedata, name='deletedata'),
	path('test/', views.test, name='test'),
]