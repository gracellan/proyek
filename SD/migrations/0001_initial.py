# Generated by Django 4.1.1 on 2023-01-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="sekolah",
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
                ("nama_sekolah", models.CharField(max_length=21)),
                ("titik_koordinat", models.CharField(max_length=50)),
                ("keterangan", models.TextField()),
            ],
        ),
    ]
