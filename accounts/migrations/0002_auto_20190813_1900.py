# Generated by Django 2.1.7 on 2019-08-13 13:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
