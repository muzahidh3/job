# Generated by Django 3.2.1 on 2021-05-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210513_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccnjobcard',
            name='problemcategory',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]