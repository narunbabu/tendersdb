# # django-rest-4-angular2 REST Framework

A simple example application where an Angular 2 app talks to an API running
Django REST framework.

## Setup

Install dependencies and run migrations to set up the app:
install virtualenvironment first
- Create a virtualenv env with "virtualenv env"
- Run `env\Scripts\activate.bat`
# And run following
## Optional
pip install Django==1.11.2
pip install djangorestframework==3.4.0
pip install pygments

## And these in tendersdb/tenders

python manage.py makemigrations dailytenders
python manage.py migrate // Creates database

# Open python Shell

python manage.py shell

# Run the following

python manage.py test

# or

from dailytenders.models import Tender
from dailytenders.serializers import TenderSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

descr='1. Supplying installation testing and commissioning of (408 kg) 6 Passenger Elevator at  Quality Control Laboratory Building Industrial Estate Borguri Tinsukia'
tend_num='AIIDC/1202/2012/260-269/18037 dt18/8/17'
start_d='31-Aug-2017 02:00 PM'
end_d='31-Aug-2017 03:00 PM'

tender = Tender(description=descr,tender_number=tend_num,
start_date=start_d,end_date=end_d)
tender.save()

You Can run through loop for all tenders

Change models.py for correct datetime format
