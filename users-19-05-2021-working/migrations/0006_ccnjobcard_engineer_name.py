# Generated by Django 3.2.1 on 2021-05-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_ccnjobcard_problemcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccnjobcard',
            name='engineer_name',
            field=models.CharField(default=False, max_length=50, null=True),
        ),
    ]
