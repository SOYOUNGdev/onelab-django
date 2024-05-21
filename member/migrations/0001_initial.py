# Generated by Django 5.0.2 on 2024-03-20 21:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('member_email', models.CharField(max_length=50)),
                ('member_school_email', models.CharField(default='<EMAIL>', max_length=50)),
                ('member_password', models.CharField(max_length=20)),
                ('member_name', models.CharField(max_length=100)),
                ('member_phone', models.CharField(max_length=30)),
                ('member_status', models.BooleanField(default=True)),
                ('member_type', models.TextField(default='oneLabProject')),
            ],
            options={
                'db_table': 'tbl_member',
            },
        ),
        migrations.CreateModel(
            name='MemberFile',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='file.file')),
                ('path', models.ImageField(upload_to='member/%Y/%m/%d')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_member_file',
            },
        ),
    ]
