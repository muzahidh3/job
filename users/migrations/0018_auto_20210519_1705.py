# Generated by Django 3.2.3 on 2021-05-19 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_printerjobcard_type_of_problem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccnjobcard',
            name='model_no',
        ),
        migrations.RemoveField(
            model_name='ccnjobcard',
            name='sr_no',
        ),
        migrations.RemoveField(
            model_name='printerjobcard',
            name='type_of_problem',
        ),
        migrations.AlterField(
            model_name='printerjobcard',
            name='ccn_job_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.ccnjobcard'),
        ),
    ]
