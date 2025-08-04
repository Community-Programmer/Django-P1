# employees/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Seeds the database with fake data'

    def handle(self, *args, **kwargs):
        from employees.models import Department, Employee
        from attendance.models import Attendance
        from performance.models import Performance
        
        fake = Faker()
        departments = ['HR', 'Engineering', 'Marketing', 'Sales']
        
        # Create Departments if they don't exist
        dept_objs = []
        for name in departments:
            dept, created = Department.objects.get_or_create(name=name)
            dept_objs.append(dept)
            if created:
                self.stdout.write(f"Created department: {name}")
        
        # Clear existing employees and related data
        Employee.objects.all().delete()
        Attendance.objects.all().delete()
        Performance.objects.all().delete()
        
        # Create 50 Employees with properly formatted phone numbers
        for _ in range(50):
            # Generate a phone number that fits in 20 characters
            phone = f"{fake.country_calling_code()}{fake.msisdn()[3:]}"
            phone = phone[:20]  # Ensure it doesn't exceed 20 characters
            
            Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=phone,
                address=fake.address(),
                date_joined=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(dept_objs)
            )
        
        # Create Attendance Records
        for emp in Employee.objects.all():
            for day in range(30):  # Last 30 days
                Attendance.objects.create(
                    employee=emp,
                    date=date.today() - timedelta(days=day),
                    status=random.choice(['P', 'A', 'L'])
                )
        
        # Create Performance Reviews
        for emp in Employee.objects.all():
            Performance.objects.create(
                employee=emp,
                rating=random.randint(1, 5),
                review_date=fake.date_between(start_date='-1y', end_date='today')
            )
            
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))