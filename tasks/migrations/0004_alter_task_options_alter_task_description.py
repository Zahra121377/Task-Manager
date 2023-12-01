# Generated by Django 4.2.7 on 2023-12-01 20:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_alter_task_due_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["due_date"]},
        ),
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.CharField(
                blank=True,
                default="I shoud do it",
                max_length=500,
                validators=[django.core.validators.MinLengthValidator(limit_value=10)],
            ),
        ),
    ]
