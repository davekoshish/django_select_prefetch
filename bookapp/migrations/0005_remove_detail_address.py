# Generated by Django 3.2.5 on 2022-09-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='address',
        ),
    ]
