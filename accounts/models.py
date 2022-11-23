from django.db import models
from django.contrib.auth.models import AbstractUser
# from mptt.fields import TreeForeignKey
# from mptt.models import MPTTModel

class User(AbstractUser):
    student_id = models.IntegerField(null=True)
    username = models.CharField(max_length=10,unique =True)
    # major = TreeForeignKey('Category',on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'username'

# class Major(MPTTModel):
#     parent = TreeForeignKey(
#         'self', related_name='children', 
#         on_delete=models.CASCADE, 
#         blank=True, null=True
#     )
#     title = models.CharField(max_length=100)
#     slug = models.SlugField(null=False, editable=False, allow_unicode=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table = 'categories'
#         ordering = ['tree_id', 'lft']
    
#     class MPTTMeta:
#         order_insertion_by = ['title']