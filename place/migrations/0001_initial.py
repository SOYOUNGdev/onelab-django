# Generated by Django 5.0.2 on 2024-03-20 21:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
        ('like', '0001_initial'),
        ('point', '__first__'),
        ('review', '__first__'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('place_title', models.CharField(max_length=30)),
                ('place_content', models.CharField(max_length=300)),
                ('place_points', models.BigIntegerField(default=1000, null=True)),
                ('place_order_status', models.BooleanField(default=False)),
                ('place_review_rating', models.FloatField(default=0.0)),
                ('place_image_file', models.ImageField(upload_to='')),
                ('place_date', models.DateField(default=django.utils.timezone.now)),
                ('place_ask_email', models.CharField(max_length=300)),
                ('place_url', models.CharField(default='http://localhost:', max_length=300)),
                ('place_post_status', models.BooleanField(default=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.school')),
            ],
            options={
                'db_table': 'tbl_place',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PlaceFile',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='file.file')),
                ('path', models.ImageField(upload_to='place/%Y/%m/%d')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='place.place')),
            ],
            options={
                'db_table': 'tbl_place_file',
            },
        ),
        migrations.CreateModel(
            name='PlaceLike',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='like.like')),
                ('place', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='place.place')),
            ],
            options={
                'db_table': 'tbl_place_like',
            },
        ),
        migrations.CreateModel(
            name='PlacePoints',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('points', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='point.point')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='place.place')),
            ],
            options={
                'db_table': 'tbl_place_points',
            },
        ),
        migrations.CreateModel(
            name='PlaceReview',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='review.review')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='place.place')),
            ],
            options={
                'db_table': 'tbl_place_review',
            },
        ),
    ]
