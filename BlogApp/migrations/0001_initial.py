# Generated by Django 3.0.3 on 2020-02-27 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=30)),
                ('userId', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForbiddenWord',
            fields=[
                ('wordId', models.IntegerField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagId', models.AutoField(primary_key=True, serialize=False)),
                ('tagName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('postTitle', models.CharField(max_length=50)),
                ('postBody', models.TextField(max_length=500)),
                ('postImage', models.ImageField(upload_to=None, verbose_name='Default')),
                ('postDatePublished', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('postDateUpdated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('postAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postCategory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BlogApp.Category')),
                ('postTag', models.ManyToManyField(blank=True, to='BlogApp.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.BooleanField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogApp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('commentContent', models.CharField(max_length=150)),
                ('commentDate', models.DateTimeField(auto_now=True)),
                ('commentAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='BlogApp.Post')),
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='BlogApp.Comment')),
            ],
        ),
    ]
