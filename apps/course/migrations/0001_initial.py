# Generated by Django 4.1.1 on 2022-09-15 16:01

import apps.course.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('image', models.ImageField(upload_to=apps.course.models.path_to_course_image)),
                ('description', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('duration', models.CharField(max_length=21)),
                ('video', models.FileField(upload_to=apps.course.models.path_to_lesson_video)),
                ('description', ckeditor.fields.RichTextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', ckeditor.fields.RichTextField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]