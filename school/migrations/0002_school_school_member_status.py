# Generated by Django 5.0.2 on 2024-03-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_member_status',
            field=models.BooleanField(default=False),
        ),
    ]
