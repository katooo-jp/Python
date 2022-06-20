# Generated by Django 4.0.5 on 2022-06-20 12:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sns.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=8, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('password_confirm', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('caption', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.users')),
            ],
            options={
                'db_table': 'posts',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Phots',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.FileField(upload_to=sns.models.media_path)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.posts')),
            ],
            options={
                'db_table': 'phots',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.users')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=100)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.users')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
