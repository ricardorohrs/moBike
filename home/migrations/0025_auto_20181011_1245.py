# Generated by Django 2.1 on 2018-10-11 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_entregaativa_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregaativa',
            name='ciclista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Ciclista'),
        ),
    ]
