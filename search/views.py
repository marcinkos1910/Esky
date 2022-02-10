from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView

from .forms import SearchForm


class SearchView(TemplateView):
    # form_class = SearchForm
    template_name = 'search/search.html'
    # success_url = reverse_lazy('search:flights')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = SearchForm(self.request.GET) if self.request.GET else SearchForm()

        return ctx

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)

        if form.is_valid():
            redirect_url = reverse('search:flights')

            return redirect(reverse('search:flights') + request.get_full_path()[1:])

        return super().get(request, *args, **kwargs)

    # def form_valid(self, form):
    #     is_valid = super().form_valid(form)
    #
    #     return is_valid


class ResultsView(TemplateView):
    # form_class = SearchForm
    template_name = 'search/results.html'
    # success_url = reverse_lazy('search:flights')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = SearchForm(self.request.GET) if self.request.GET else SearchForm()

        return ctx


class ResultsAjaxView(TemplateView):
    template_name = 'search/results_ajax.html'

