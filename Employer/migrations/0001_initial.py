# Generated by Django 4.0.3 on 2022-03-09 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(upload_to='images')),
                ('website', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('number_of_employees', models.CharField(choices=[('less than 200', 'less than 200'), ('200 to 500', '200 to 500'), ('500 to 1000', '500 to 1000'), ('more than 1000', 'more than 1000')], max_length=50)),
                ('services', models.CharField(choices=[('software services', 'software services'), ('training services', 'training services'), ('event planning services', 'event planning services'), ('consulting services', 'consulting services'), ('marketing services', 'marketing services'), ('construction services', 'construction services'), ('legal services', 'legal services'), ('delivery services', 'delivery services'), ('real estate services', 'real estate services'), ('health care services', 'health care services'), ('education', 'education'), ('other', 'other')], max_length=500)),
                ('Designation', models.CharField(choices=[('HR', 'HR'), ('Manager', 'Manager'), ('Recruiter', 'Recruiter'), ('Consultant', 'Consultant'), ('Administrator', 'Administrator'), ('Analyst', 'Analyst')], default='HR', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('role', models.CharField(choices=[('employer', 'employer'), ('applicant', 'applicant')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=150)),
                ('salary', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField(max_length=1000)),
                ('experience', models.PositiveIntegerField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=500)),
                ('vacancies', models.PositiveIntegerField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.companyprofile')),
            ],
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='Employer.myuser'),
        ),
    ]
