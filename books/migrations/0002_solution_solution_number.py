# Generated by Django 2.2 on 2019-04-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
