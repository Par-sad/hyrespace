# Generated by Django 2.0 on 2018-10-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcript',
            name='transcript_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
