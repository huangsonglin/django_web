# Generated by Django 2.1.3 on 2019-11-27 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='功能名字')),
                ('desc', models.CharField(max_length=30, null=True, verbose_name='功能介绍')),
            ],
            options={
                'verbose_name': '功能名字',
                'verbose_name_plural': '功能名字',
            },
        ),
    ]
