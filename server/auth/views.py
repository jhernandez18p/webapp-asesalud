from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import SignUpForm


class SignUp(FormView):
    template_name = 'auth/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal
        user.profile.birth_date = form.cleaned_data.get('birth_date')
        user.save()
        
        return super().form_valid(form)


"""
Customizing error views
"""
def my_custom_bad_request_view(request, exception):
    return HttpResponse('bad request')


def my_custom_permission_denied_view(request, exception):
    return HttpResponse('permission denied')


def my_custom_page_not_found_view(request, exception):
    return HttpResponse('page not found')


def my_custom_error_view(request):
    return HttpResponse('error')