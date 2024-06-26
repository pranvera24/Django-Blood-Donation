# Generated by Django 5.0.4 on 2024-04-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receivers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='user',
        ),
        migrations.AddField(
            model_name='receiver',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receiver',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='receiver',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='receiver',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='receiver',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='receiver',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='receiver',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
