# Generated by Django 4.1.5 on 2023-01-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Panel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("color", models.CharField(max_length=100)),
            ],
        ),
    ]
