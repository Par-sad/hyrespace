# Generated by Django 2.0 on 2018-10-04 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_transcript_transcript_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transcript',
            options={'ordering': ['transcript_name']},
        ),
    ]
