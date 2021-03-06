# Generated by Django 3.2.6 on 2021-11-29 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_post_text_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='prod_default_image.png', upload_to='event_icons/'),
        ),
    ]
