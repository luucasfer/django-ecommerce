# Generated by Django 5.1.1 on 2024-09-21 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userauths", "0002_user_bio"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user", options={"verbose_name_plural": "Usuários"},
        ),
    ]
