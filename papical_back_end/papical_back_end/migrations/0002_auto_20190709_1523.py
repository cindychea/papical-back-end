# Generated by Django 2.2.3 on 2019-07-09 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('papical_back_end', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangout',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]