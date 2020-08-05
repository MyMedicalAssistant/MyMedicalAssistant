from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  first_name = models.CharField(max_length = 64)
  last_name = models.CharField(max_length = 64)
  email=models.EmailField(('email address'), blank=True, unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
    return self.username


# Create your models here.
# class MyAccountManager(BaseUserManager):
# 	def create_user(self, email, username, password = None):
# 		if not email:	
# 			raise ValueError("Users must have email")
# 		if not username:
# 			raise ValueError("Users need username")
# 		user = self.model(
# 			email = self.normalize_email(email),
# 			username=username,
# 		)
#     user.set_password(password)
#     user.save(using = self._db)
#     return user

#   def create_superuser(self, email, username, password):
#   	user = self.create_user(
#       email = self.normalize_email(email),
#       password = password,
#       username = username,
# 	  )
#     user.is_admin = True
#     user.is_staff = True
#     user.is_superuser = True
#     user.save(using=self._db)
#     return user

# class CustomUser(AbstractUser):
# 	email = models.EmailField(verbose_name = 'email', max_length = 60, unique=True)
# 	username = models.CharField(max_length=30, unique = True)
# 	date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
#   is_admin = models.BooleanField(default = False)
# 	is_active = models.BooleanField(default = True)
# 	is_staff = models.BooleanField(default=False)
# 	is_superuser = models.BooleanField(default = False)
#   is_doctor = models.BooleanField(default = False)
# 	first_name = models.CharField(max_length = 64)
# 	last_name = models.CharField(max_length = 64)
	
# 	USERNAME_FIELD = 'email'
# 	REQUIRED = ['username']
	
# 	objects = MyAccountManager()

# 	def __str__(self):
# 		return self.username
# 	def has_perm(self, perm, obj=None):
# 		return self.is_doctor