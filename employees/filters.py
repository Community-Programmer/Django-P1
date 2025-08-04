import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    date_joined = django_filters.DateFromToRangeFilter()
    
    class Meta:
        model = Employee
        fields = ['department', 'date_joined']