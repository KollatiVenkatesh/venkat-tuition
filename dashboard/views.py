from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import Student
from staff.models import Staff, StaffAttendance
from fees.models import Fee
from django.utils.timezone import now
from django.db.models import Sum
from django.contrib.auth.decorators import user_passes_test

def is_owner(user):
    return user.is_superuser

@user_passes_test(is_owner)
def owner_dashboard(request):
    today = now().date()

    total_students = Student.objects.count()
    active_students = Student.objects.filter(is_active=True).count()

    total_staff = Staff.objects.count()
    staff_present_today = StaffAttendance.objects.filter(
        date=today, status="Present"
    ).count()

    total_collected = Fee.objects.aggregate(
        total=Sum('paid_amount')
    )['total'] or 0

    total_pending = (
        Fee.objects.aggregate(
            total=Sum('total_amount')
        )['total'] or 0
    ) - total_collected

    context = {
        "total_students": total_students,
        "active_students": active_students,
        "total_staff": total_staff,
        "staff_present_today": staff_present_today,
        "total_collected": total_collected,
        "total_pending": total_pending,
    }

    return render(request, "dashboard/owner_dashboard.html", context)

from django.contrib.auth.decorators import login_required
from staff.models import StaffAttendance
from django.utils.timezone import now

@login_required
def staff_dashboard(request):
    today = now().date()

    attendance_today = StaffAttendance.objects.filter(
        staff__user=request.user,
        date=today
    ).first()

    context = {
        "attendance": attendance_today
    }

    return render(request, "dashboard/staff_dashboard.html", context)
