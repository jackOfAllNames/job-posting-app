from django.shortcuts import render, HttpResponse, get_object_or_404
from job_board.models import JobPosting

# Create your views here.
def index(request):
    active_postings = JobPosting.objects.filter(is_active=True)
    context = {
        "job_postings": active_postings
    }
    return render(request, "job_board/index.html", context)

def job_details(request, pk):
    # job_posting = JobPosting.objects.get(pk=pk)
    job_posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {
        "posting": job_posting
    }
    return render(request, "job_board/detail.html", context)
