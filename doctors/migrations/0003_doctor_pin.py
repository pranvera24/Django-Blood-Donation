# Generated by Django 5.0.3 on 2024-04-03 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_remove_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='pin',
            field=models.CharField(default='0000', max_length=10),
        ),
    ]
