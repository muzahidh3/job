# Generated by Django 3.2.3 on 2021-05-20 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210520_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printerjobcard',
            old_name='printer_problem',
            new_name='problem',
        ),
    ]