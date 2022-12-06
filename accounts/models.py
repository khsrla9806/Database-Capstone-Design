from django.db import models
from django.contrib.auth.models import AbstractUser
# from mptt.fields import TreeForeignKey
# from mptt.models import MPTTModel

class User(AbstractUser):
    student_id = models.CharField(max_length=9, null=False, unique =True)
    username = models.CharField(max_length=10,  default='', null=False)
    # major = TreeForeignKey('Category',on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['username']