# Generated by Django 3.2.1 on 2021-05-12 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_ccnjobcard_engineer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ccnjobcard',
            old_name='engineer_name',
            new_name='assigned_to',
        ),
    ]