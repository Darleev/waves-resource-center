# Generated by Django 3.1 on 2020-09-24 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Enter a URL-friendly name', unique=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Enter a URL-friendly name', unique=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Enter a URL-friendly name', unique=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('summary', models.TextField(blank=True, max_length=200, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField(help_text='Enter the video URL here', verbose_name='URL')),
                ('authors', models.ManyToManyField(related_name='core_video_authors', related_query_name='core_video_author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.category')),
                ('tags', models.ManyToManyField(blank=True, help_text='Select some tags for this resource', related_name='core_video_tags', related_query_name='core_video_tag', to='core.Tag')),
            ],
            options={
                'ordering': ['-date_posted'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Enter a URL-friendly name', unique=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('summary', models.TextField(blank=True, max_length=200, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('cover_image', models.ImageField(default='book-cover.png', help_text="Upload the book's cover here", upload_to='book_covers')),
                ('file_upload', models.FileField(help_text='Upload the book here', upload_to='books')),
                ('authors', models.ManyToManyField(related_name='core_book_authors', related_query_name='core_book_author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.category')),
                ('tags', models.ManyToManyField(blank=True, help_text='Select some tags for this resource', related_name='core_book_tags', related_query_name='core_book_tag', to='core.Tag')),
            ],
            options={
                'ordering': ['-date_posted'],
                'abstract': False,
            },
        ),
    ]
