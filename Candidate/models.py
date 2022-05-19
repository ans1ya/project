from django.db import models
from Employer.models import MyUser,Jobs

# Create your models here.
class Applicant(models.Model):
    applicant=models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name='applicant')
    applicant_name=models.CharField(max_length=100,null=True)
    profile_pic=models.ImageField(upload_to='images')
    qualification=models.CharField(max_length=50,null=True)
    exp=(
        ('0-1','o-1'),
        ('2-5','2-5'),
        ('5-6','5-6'),
        ('6-8','6-8'),
        ('8-10','8-10'),
        ('more than 10','more than 10')
    )
    experience=models.CharField(max_length=50,choices=exp)
    skills=models.CharField(max_length=1000,null=True)
    resume=models.FileField(upload_to='files')


class Applications(models.Model):
    applicant=models.ForeignKey(Applicant,on_delete=models.CASCADE)
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    submitted_date=models.DateField(auto_now_add=True,null=True)
    options=(

        ('accepted','accepted'),
        ('rejected','rejected'),
        ('under_processing','under_processing')

    )
    status=models.CharField(max_length=50,choices=options,default='under_processing')
    status_updated_date=models.DateField(null=True)