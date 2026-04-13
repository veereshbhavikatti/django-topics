from django.db import models

class JobApplications(models.Model):

    class JobType(models.TextChoices):
        FULL_TIME = 'full_time', 'Full Time'
        PART_TIME = 'part_time', 'Part Time'
        INTERNSHIP = 'internship', 'Internship'

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField()
    job_type = models.CharField(max_length=20, choices=JobType.choices)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name