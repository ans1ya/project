# Generated by Django 4.0.3 on 2022-03-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0002_applicant_applicant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='skills',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
