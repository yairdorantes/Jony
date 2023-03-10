# Generated by Django 4.1.1 on 2023-02-04 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('phone', models.IntegerField(verbose_name='Numero telefonico')),
                ('message', models.TextField(verbose_name='Mensaje')),
            ],
        ),
    ]
