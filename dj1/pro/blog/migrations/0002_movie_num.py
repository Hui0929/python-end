# Generated by Django 2.1.7 on 2019-04-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='num',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
