# Generated by Django 4.1.5 on 2023-01-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("dateOfUpload", models.DateField(auto_now=True)),
                ("price", models.FloatField(blank=True)),
                ("condition", models.CharField(blank=True, max_length=30)),
                ("brand", models.CharField(blank=True, max_length=30)),
                ("descriptionText", models.TextField(blank=True)),
                ("available", models.BooleanField(blank=True)),
                ("tags", models.ManyToManyField(blank=True, to="products.tag")),
            ],
        ),
    ]
