# Generated by Django 2.2.3 on 2019-07-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papical_back_end', '0003_auto_20190709_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]