from django.shortcuts import render
from .models import Faq


def faq_list(request):
    """Вывод списка faq app
    """
    faq = Faq.objects.all()
    return render(request, "faq/faq_list.html", {"faqs": faq})
