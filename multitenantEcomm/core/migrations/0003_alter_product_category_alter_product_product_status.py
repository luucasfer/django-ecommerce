# Generated by Django 5.1.1 on 2024-09-21 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_address_options_alter_cartorder_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="category",
                to="core.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_status",
            field=models.CharField(
                choices=[
                    ("desabilitado", "Desabilitado"),
                    ("em analise", "Em analise"),
                    ("publicado", "Publicado"),
                ],
                default="publicado",
                max_length=20,
            ),
        ),
    ]
