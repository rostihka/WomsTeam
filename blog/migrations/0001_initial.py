# Generated by Django 2.0.1 on 2018-01-26 01:37

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
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=50, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('published_date', models.DateTimeField(
                    blank=True, null=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('mini_text', models.TextField(
                    max_length=200, verbose_name='Краткое содержание')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('created_date', models.DateTimeField(
                    auto_now_add=True, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(
                    blank=True, null=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True,
                                            upload_to='blog/', verbose_name='Изображение')),
                ('description', models.CharField(max_length=50,
                                                 null=True, verbose_name='Описание страницы')),
                ('keywords', models.CharField(max_length=50,
                                              null=True, verbose_name='Ключивае слова страницы')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Автор')),
                ('category',
                 models.ForeignKey(blank=True,
                                   null=True,
                                   on_delete=django.db.models.deletion.SET_NULL,
                                   to='blog.Category',
                                   verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50,
                                         unique=True, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(
                blank=True, to='blog.Tag', verbose_name='Тег'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='blog.Post',
                verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор'),
        ),
    ]
