# Generated by Django 3.2.7 on 2021-10-07 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0003_invite"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="post",
            name="updated_by",
        ),
    ]