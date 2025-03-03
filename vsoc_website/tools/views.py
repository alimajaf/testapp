from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib import messages

def home(request ):
    return render(request, 'tools/home.html', {} )

def sessions(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    if request.user.is_authenticated:
        #convert month to number
        month = month.title()
        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)

        #create calendar
        cal = HTMLCalendar().formatmonth(
            year,
            month_number
            )

        #show the current time
        today = datetime.now().date
        now = datetime.now().ctime

        return render(request, 'tools/sessions.html', {
            "year": year,
            "month": month,
            "cal": cal,
            "today": today,
            "now": now,
        } )
    
    else:
        messages.success(request, ("Please log in to view this page!"))
        return redirect('home')