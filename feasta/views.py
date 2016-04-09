from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from feasta.models import *
from feasta.config import *
from feasta.forms import *
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.debug import sensitive_post_parameters

class Home(TemplateView):
	template_name = 'home.html'
	def get_context_data(self,**kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		return context
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		if not self.request.user.is_active:
			return HttpResponseRedirect(settings.LOGIN_URL)
		return super(Home,self).dispatch(*args,**kwargs)
class Login(FormView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = settings.LOGIN_REDIRECT_URL
		
	def form_valid(self,form):
		redirect_to = settings.LOGIN_REDIRECT_URL
        	login(self.request, form.get_user())
        	if self.request.session.test_cookie_worked():
           		self.request.session.delete_test_cookie()
        	return HttpResponseRedirect(redirect_to) 
	
	def form_invalid(self,form):	
		return super(Login, self).form_invalid(form)
	@method_decorator(sensitive_post_parameters())	
	def dispatch(self, *args, **kwargs):
		if self.request.user.is_active:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
		return super(Login,self).dispatch(*args, **kwargs)
	def get_context_data(self, **kwargs):
			context = super(Login,self).get_context_data(**kwargs)
			return context

class UnregisterView(FormView):
	form_class = UnregisterForm
	template_name = 'unregister.html'
class BulkUnregisterView(FormView):
	form_class = BulkUnregisterForm
	template_name = 'bulkunregister.html'
				
class MenuView(TemplateView):
	template_name = 'menu.html'
class MyAccount(TemplateView):	
	template_name = 'myaccount.html'

class ListForMeal(TemplateView):
	template_name = 'listformeal.html'	