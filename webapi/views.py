from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Stream
from .forms import StreamForm

class IndexView(ListView):
    template_name = 'streams/index.html'

    def get_queryset(self):
        return Stream.objects.order_by('title')

def streams(request):
    return render(request, 'streams/index.html', {'stream_list': IndexView.get_queryset()})

class DetailView(DetailView):
    model = Stream
    template_name = 'streams/detail.html'

def create_stream(request):
    if request.method == 'POST':
        form = StreamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(streams))
    else:
        form = StreamForm()

    return render(request, 'streams/create.html', {'form': form}) # TODO: transfer error_message

def update_stream(request, stream_id):
    stream = get_object_or_404(Stream, pk=stream_id)
    if request.method == 'POST':
        form = StreamForm(request.POST, instance=stream)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(streams))
    else:
        form = StreamForm(stream)
    
    return render(request, 'streams/detail.html', {'stream': stream})