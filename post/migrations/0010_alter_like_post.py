# Generated by Django 3.2.6 on 2021-11-30 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='post.post'),
        ),
    ]
