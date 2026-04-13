from django.shortcuts import render, redirect
from .forms import JobApplicationForm


def job_application_view(request):

    form = JobApplicationForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():
        form.save()
        return redirect('success')

    return render(
        request,
        'applications/apply.html',
        {'form': form}
    )


def success(request):
    return render(
        request,
        'applications/success.html'
    )