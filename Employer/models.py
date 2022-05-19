from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class MyUserManager(BaseUserManager):
    def create_user(self, email,role, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,role,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            role=role
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    options=(
        ('employer','employer'),
        ('applicant','applicant')
    )
    role=models.CharField(max_length=20,choices=options,null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class CompanyProfile(models.Model):
    company=models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name='employer')
    company_name=models.CharField(max_length=30,null=True)
    company_logo=models.ImageField(upload_to='images')
    recruter_name=models.CharField(max_length=50,null=True)
    designation = (
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('Recruiter', 'Recruiter'),
        ('Consultant', 'Consultant'),
        ('Administrator', 'Administrator'),
        ('Analyst', 'Analyst')
    )
    Designation = models.CharField(max_length=100, choices=designation, default='HR')
    website=models.CharField(max_length=100)
    start_date=models.DateField()
    options=(
        ('less than 200','less than 200'),
        ('200 to 500','200 to 500'),
        ('500 to 1000','500 to 1000'),
        ('more than 1000','more than 1000')
    )
    number_of_employees=models.CharField(max_length=50,choices=options,default='less than 200')
    selections=(
        ('software services','software services'),
        ('training services','training services'),
        ('event planning services','event planning services'),
        ('consulting services','consulting services'),
        ('marketing services','marketing services'),
        ('construction services','construction services'),
        ('legal services','legal services'),
        ('delivery services','delivery services'),
        ('real estate services','real estate services'),
        ('health care services','health care services'),
        ('education','education'),
        ('other','other')
    )
    services = models.CharField(max_length=500,choices=selections,default='other')
    Bio=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.company_name


class Jobs(models.Model):
    company=models.ForeignKey(CompanyProfile,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=150)
    salary=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images')
    description=models.TextField(max_length=1000)
    experience=models.PositiveIntegerField()
    location=models.CharField(max_length=100)
    skills=models.CharField(max_length=500)
    vacancies=models.PositiveIntegerField()
    create_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.job_title