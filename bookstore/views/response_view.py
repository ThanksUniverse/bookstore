from django.views import generic
from bookstore.models import Response

class ResponseView(generic.ListView):
    queryset = Response.objects.order_by('-created_at')
    template_name = "index.html"