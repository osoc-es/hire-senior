# Generated by Django 3.2.5 on 2021-07-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20210713_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_postal_code',
        ),
        migrations.AddField(
            model_name='company',
            name='company_date_registered',
            field=models.DateTimeField(db_column='date_registered', null=True),
        ),
    ]
