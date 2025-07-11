from django.shortcuts import render, HttpResponse
from job_board.models import JobPosting

# Create your views here.
def index(request):
    non_active_postings = JobPosting.objects.filter(is_active=False)
    context = {
        "job_postings": non_active_postings
    }
    return render(request, "job_board/index.html", context)
