from django.test import TestCase

# Create your tests here.
from models import *

author_list = AuthorInfo.objects.all()
print author_list

