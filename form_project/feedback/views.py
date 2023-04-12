from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackFrom
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

class FeedbackView(FormView):
    form_class = FeedbackFrom
    template_name = 'feedback/feedback.html'
    success_url = '/done'

    def form_valid(self, form):
        form.save()
        return super(FeedbackView, self).form_valid(form)


# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackFrom()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackFrom(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(View):
    def get(self, request):
        return render(request, 'feedback/done.html')


class UpdateFeedbackView(View):
    def get(self, request, id_feed):
        feed = Feedback.objects.get(id=id_feed)
        form = FeedbackFrom(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feed):
        feed = Feedback.objects.get(id=id_feed)
        form = FeedbackFrom(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
        form = FeedbackFrom(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})


# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['all_feeds'] = Feedback.objects.all()
#         return context
class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'all_feeds'


class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    context_object_name = 'current'

#
# def index(request):
#     if request.method == 'POST':
#         form = FeedbackFrom(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     form = FeedbackFrom()
#     return render(request, 'feedback/feedback.html', context={'form': form})

# def update_feed(request, id_feed):
#     feed = Feedback.objects.get(id=id_feed)
#     if request.method == 'POST':
#         form = FeedbackFrom(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     form = FeedbackFrom(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})

# Crea
