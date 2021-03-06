# Generated by Django 3.1.5 on 2021-01-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.IntegerField()),
                ('name', models.CharField(max_length=120)),
                ('designation', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=120)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
