# Generated by Django 4.1.7 on 2023-04-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_delete_temp_lstm_adilabadd"),
    ]

    operations = [
        migrations.CreateModel(
            name="TEMP_LSTM_ADILABADD",
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
                ("district", models.TextField(null=True)),
                ("mandal", models.TextField(null=True)),
                ("date", models.DateField(null=True)),
                ("temp", models.FloatField(null=True)),
            ],
        ),
    ]
