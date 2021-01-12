from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from .form import SignUpForm, LoginForm


class Signup(FormView):
    form_class= SignUpForm
    template_name= "signup.html"
    success_url="/login"

    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    # def form_invalid(self,form):
    #     import pdb;pdb.set_trace()

class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = "/dashboard"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):
       login(self.request, form.get_user())
       return HttpResponseRedirect(self.get_success_url())

# @method_decorator(melogin_required)
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    # def form_invalid(self,form):
    #     import pdb;pdb.set_trace()