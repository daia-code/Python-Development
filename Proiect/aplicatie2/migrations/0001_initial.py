# Generated by Django 4.0.4 on 2022-05-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=50)),
                ('tip_companie', models.CharField(choices=[('SRL', 'S.R.L.'), ('SA', 'S.A.')], max_length=10)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]
