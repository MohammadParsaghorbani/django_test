# Generated by Django 5.1.1 on 2024-09-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_publish_day_alter_post_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='توضیحات',
            field=models.TextField(blank=True, null=True),
        ),
    ]
