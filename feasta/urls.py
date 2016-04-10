from django.conf.urls import url
from feasta.views import *
from feasta.forms import PasswordChangeForm
from django.conf import settings
from django.contrib.auth.views import logout, password_change
from django.contrib.auth.decorators import login_required

urlpatterns = [
			url(r'^$',
				login_required(Home.as_view())),

			url(r'^accounts/login/$', 
				Login.as_view()),

			url(r'^unregister/$', 
				login_required(UnregisterView.as_view())),

			url(r'^bulkunregister/$', 
				login_required(BulkUnregisterView.as_view())),

			url(r'^menu/$', 
				login_required(MenuView.as_view())),

			url(r'^accounts/edit-profile/$', 
				login_required(EditProfile.as_view())),

			url(r'^getlist/today/$', 
				login_required(ListForMeal.as_view())),

			url(r'^accounts/signout/$', 
				login_required(logout), 
				kwargs={'next_page':settings.LOGOUT_URL },	
				name='logout'), 

			url(r'^accounts/change-password/$', 
				login_required(password_change), 
				name='passwordchange',
				kwargs={'post_change_redirect':settings.LOGIN_URL,
					    'template_name':'passwordchange.html',
					    'password_change_form':PasswordChangeForm
				})
		]