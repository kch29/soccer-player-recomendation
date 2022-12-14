# Generated by Django 4.0 on 2022-09-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_setting', '0002_defensive'),
    ]

    operations = [
        migrations.CreateModel(
            name='passing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('position1', models.CharField(max_length=20)),
                ('position2', models.CharField(max_length=20)),
                ('Apps', models.CharField(max_length=20)),
                ('Mins', models.FloatField()),
                ('Assists', models.FloatField()),
                ('KeyP', models.FloatField()),
                ('AvgP', models.FloatField()),
                ('PSpercent', models.FloatField()),
                ('Crosses', models.FloatField()),
                ('LongB', models.FloatField()),
                ('ThrB', models.FloatField()),
                ('Rating', models.FloatField()),
            ],
        ),
    ]
