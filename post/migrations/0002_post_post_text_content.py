# Generated by Django 3.2.6 on 2021-11-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_text_content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
