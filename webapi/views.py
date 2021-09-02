from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Stream

class IndexView(generic.ListView):
    template_name = 'streams/index.html'

    def get_queryset(self):
        return Stream.objects.order_by('title')

def streams(request):
    return render(request, 'streams/index.html', {'stream_list': IndexView.get_queryset()})

class DetailView(generic.DetailView):
    model = Stream
    template_name = 'streams/detail.html'

def update_stream(request, stream_id):
    stream = get_object_or_404(Stream, pk=stream_id)
    try:
        stream_new_title = request.POST['title']
        stream_new_code = request.POST['code']
        stream_new_description = request.POST['description']
    except (KeyError):
        return render(request, 'streams/detail.html', {'stream': stream})
    else: 
        stream.title = stream_new_title
        stream.code = stream_new_code       
        stream.description = stream_new_description
        stream.save()
        return HttpResponseRedirect(reverse(streams))