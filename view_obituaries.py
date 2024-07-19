# views.py
from django.core.paginator import Paginator
from .models import Obituary

def view_obituaries(request):
    obituaries = Obituary.objects.all().order_by('-submission_date')
    paginator = Paginator(obituaries, 10)  # 10 obituaries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_obituaries.html', {'page_obj': page_obj})