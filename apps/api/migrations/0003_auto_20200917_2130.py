# Generated by Django 3.1.1 on 2020-09-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200917_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='links',
            field=models.ManyToManyField(blank=True, related_name='added', to='api.Link'),
        ),
    ]