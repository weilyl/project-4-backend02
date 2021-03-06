# Generated by Django 3.1.1 on 2020-09-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('notes', models.TextField(max_length=1000)),
                ('difficulty', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='link',
            name='list',
        ),
        migrations.AddField(
            model_name='list',
            name='links',
            field=models.ManyToManyField(null=True, related_name='added', to='api.Link'),
        ),
    ]
