# Generated by Django 4.1.5 on 2023-03-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wcapi', '0004_logins'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='month',
            field=models.CharField(default='dec', max_length=255),
        ),
    ]
