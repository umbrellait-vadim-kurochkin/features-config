from django.shortcuts import render

def stream_list(request):
    return render(request, 'streams/stream_list.html', {})
