# Generated by Django 5.0.2 on 2024-03-20 21:57

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
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('notification_title', models.CharField(max_length=30)),
                ('notification_content', models.CharField(max_length=2000)),
                ('notification_view_count', models.IntegerField(default=0)),
                ('notification_status', models.SmallIntegerField(choices=[(0, '커뮤니티'), (1, '원랩'), (2, '장소공유'), (3, '대회공모전')], default=0)),
                ('notification_post_status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_notification',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NotificationFile',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='file.file')),
                ('path', models.ImageField(upload_to='notification/%Y/%m/%d')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notification.notification')),
            ],
            options={
                'db_table': 'tbl_notification_file',
            },
        ),
    ]
