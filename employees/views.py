from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import EmployeeFilter
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department__name', 'date_joined']
    search_fields = ['name', 'email']
    ordering_fields = ['date_joined', 'name']
    filterset_class = EmployeeFilter

class DepartmentStatsView(APIView):
    def get(self, request):
        stats = Department.objects.annotate(
            employee_count=Count('employee')
        ).values('name', 'employee_count')
        
        labels = [item['name'] for item in stats]
        values = [item['employee_count'] for item in stats]
        
        return Response({'labels': labels, 'values': values})

class AttendanceStatsView(APIView):
    def get(self, request):
        from attendance.models import Attendance
        from django.db.models import Count, Case, When, IntegerField
        from django.utils import timezone
        from datetime import timedelta
        
        # Get last 30 days data
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=30)
        
        # Generate date range
        dates = [start_date + timedelta(days=i) for i in range(31)]
        
        # Prepare data structure
        results = []
        for date in dates:
            day_data = Attendance.objects.filter(date=date).aggregate(
                present=Count(Case(When(status='P', then=1), output_field=IntegerField())),
                absent=Count(Case(When(status='A', then=1), output_field=IntegerField())),
                late=Count(Case(When(status='L', then=1), output_field=IntegerField()))
            )
            results.append({
                'date': date,
                **day_data
            })
        
        return Response(results)

# employees/views.py
from django.shortcuts import render
from django.db.models import Count, Case, When, IntegerField
from .models import Department
from attendance.models import Attendance
from datetime import timedelta
from django.utils import timezone

def charts_view(request):
    # Get department stats
    dept_stats = Department.objects.annotate(
        employee_count=Count('employee')
    ).values('name', 'employee_count')
    
    # Get attendance stats for last 30 days
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=30)
    dates = [start_date + timedelta(days=i) for i in range(31)]
    
    attendance_data = []
    for date in dates:
        day_stats = Attendance.objects.filter(date=date).aggregate(
            present=Count(Case(When(status='P', then=1), output_field=IntegerField())),
            absent=Count(Case(When(status='A', then=1), output_field=IntegerField())),
            late=Count(Case(When(status='L', then=1), output_field=IntegerField()))
        )
        attendance_data.append({
            'date': date.strftime('%Y-%m-%d'),
            **day_stats
        })
    
    context = {
        'dept_stats': list(dept_stats),
        'attendance_data': attendance_data
    }
    return render(request, 'charts.html', context)


def welcome_view(request):
    return render(request, 'welcome.html')