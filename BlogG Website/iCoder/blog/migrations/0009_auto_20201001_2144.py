# Generated by Django 3.1.1 on 2020-10-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201001_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]