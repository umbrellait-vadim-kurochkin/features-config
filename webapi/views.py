from django.shortcuts import render

def stream_list(request):
    return render(request, 'templates/stream_list.html', {})
