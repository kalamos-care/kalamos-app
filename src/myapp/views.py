from django.views.generic import TemplateView
from .tasks import show_hello_world
from .models import Profile
# Create your views here.


class ShowHelloWorld(TemplateView):
    template_name = 'hello_world.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_content'] = Profile.objects.all()
        return context
