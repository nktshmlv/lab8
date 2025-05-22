from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Call, Client, Reason, Operator, Tag
from .forms import CallForm

class CallListView(ListView):
    model = Call
    template_name = 'calls/call_list.html'
    context_object_name = 'calls'

class CallDetailView(DetailView):
    model = Call
    template_name = 'calls/call_detail.html'

class CallCreateView(CreateView):
    model = Call
    form_class = CallForm
    template_name = 'calls/call_form.html'
    success_url = reverse_lazy('call_list')

class CallUpdateView(UpdateView):
    model = Call
    form_class = CallForm
    template_name = 'calls/call_form.html'
    success_url = reverse_lazy('call_list')

class CallDeleteView(DeleteView):
    model = Call
    template_name = 'calls/call_confirm_delete.html'
    success_url = reverse_lazy('call_list')