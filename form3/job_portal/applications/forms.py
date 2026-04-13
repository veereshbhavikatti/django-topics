from django import forms
from .models import JobApplications
import re

class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplications
        fields = '__all__'

    # 1️⃣ Name Validation
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")

        return name

    # 2️⃣ Email Validation
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("Only Gmail is allowed")

        return email

    # 3️⃣ Phone Validation
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not re.match(r'^[0-9]{10}$', phone):
            raise forms.ValidationError("Phone must be 10 digits")

        return phone

    # 4️⃣ Resume Validation
    def clean_resume(self):
        resume = self.cleaned_data.get('resume')

        if resume:
            if not resume.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF file allowed")

        return resume

    # 5️⃣ Global Validation
    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        job_type = cleaned_data.get('job_type')

        if name and job_type:
            if name.lower() == "admin":
                raise forms.ValidationError(
                    "Admin cannot apply for jobs"
                )

        return cleaned_data