# Generated by Django 4.0.4 on 2022-06-22 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='corretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calcular_salario', models.CharField(max_length=100)),
            ],
        ),
    ]
