# Generated by Django 4.0.4 on 2022-06-22 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='renovacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataDesoculpacao', models.CharField(max_length=100)),
                ('dataRenovacao', models.CharField(max_length=100)),
                ('cartorio', models.CharField(max_length=100)),
            ],
        ),
    ]
