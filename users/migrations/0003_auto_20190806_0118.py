# Generated by Django 2.2 on 2019-08-06 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_password1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password1',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='testPassword', max_length=150),
        ),
    ]
