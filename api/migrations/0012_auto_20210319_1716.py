# Generated by Django 3.1.7 on 2021-03-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210316_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abort', models.BooleanField(default=False)),
                ('delMapData', models.BooleanField(default=False)),
                ('delData', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now=True, verbose_name='time')),
            ],
        ),
        migrations.DeleteModel(
            name='Abort',
        ),
    ]
