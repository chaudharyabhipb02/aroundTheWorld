# Generated by Django 2.2.3 on 2019-10-01 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='name',
            new_name='name1',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='date',
        ),
    ]
