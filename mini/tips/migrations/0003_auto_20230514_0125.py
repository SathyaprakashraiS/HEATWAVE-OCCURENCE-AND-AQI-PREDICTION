# Generated by Django 3.2.18 on 2023-05-13 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0002_auto_20230514_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tips',
            name='maxvaluerange',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tips',
            name='minvaluesrange',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]