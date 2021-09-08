from django.test import TestCase
from django.urls import reverse

from .models import Stream

class StreamIndexViewTests(TestCase):
    def test_no_streams(self):
        """
        If no streams exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('stream_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No streams are available.")
        self.assertQuerysetEqual(response.context['stream_list'], [])

    def test_some_streams(self):
        """
        Streams are displayed on the index page.
        """
        streamA = Stream.objects.create()
        streamB = Stream.objects.create()
        
        response = self.client.get(reverse('stream_list'))
        self.assertQuerysetEqual(
            response.context['stream_list'],
            [streamA, streamB],
        )

class StreamDetailViewTests(TestCase):
    def test_no_streams(self):
        # The detail view of a stream with no streams in db returns a 404 not found.
        url = reverse('stream_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_some_stream(self):
        # The detail view of a stream displays the title text.
        stream = Stream.objects.create()
        url = reverse('stream_detail', args=(stream.id,))
        response = self.client.get(url)
        self.assertContains(response, stream.title)