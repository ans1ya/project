from Employer.models import Jobs
from Candidate.models import Applicant,Applications
import django_filters

class JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter( lookup_expr='contains')
    skills=django_filters.CharFilter(lookup_expr='contains')
    location=django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model=Jobs
        fields=['job_title','skills','location']
