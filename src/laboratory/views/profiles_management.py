from django.views.generic import ListView, UpdateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from laboratory.decorators import user_group_perms

from laboratory.models import Profile
from laboratory.forms import ProfileForm


class ProfilesListView(LoginRequiredMixin, ListView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.filter(laboratories__id=self.kwargs['lab_pk'])
        context['lab_pk'] = self.kwargs['lab_pk']
        return context


class ProfileUpdateView(LoginRequiredMixin, FormView):
    template_name = 'laboratory/profile_form.html'
    form_class = ProfileForm
    model = Profile

    def get_context_data(self, **kwargs):
        context = dict()
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['profile_form'] = ProfileForm(initial=
            {
                'first_name': profile.user.first_name,
                'last_name': profile.user.last_name,
                'id_card': profile.id_card,
                'job_position': profile.job_position,
                'profile_id': profile.id
            }
        )
        context['lab_pk'] = self.kwargs['lab_pk']

        return context

    def get_success_url(self, **kwargs):
        lab_pk = self.kwargs['lab_pk']
        success_url = f'/lab/{lab_pk}/profiles/list'
        return success_url

    
    def form_valid(self, form):
        response = super().form_valid(form)
        profile_id = form.cleaned_data.get('profile_id')
        profile = Profile.objects.get(pk=profile_id)

        profile.id_card = form.cleaned_data.get('id_card')
        profile.job_position = form.cleaned_data.get('job_position')
        profile.user.first_name = form.cleaned_data.get('first_name')
        profile.user.last_name = form.cleaned_data.get('last_name')
        profile.user.save()
        profile.save()
        
        return response