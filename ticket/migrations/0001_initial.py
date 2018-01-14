# Generated by Django 2.0 on 2017-12-22 18:26

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
                ('kat', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=100, verbose_name='Тема')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('created', models.DateTimeField(
                    auto_now_add=True, verbose_name='Дата создания')),
                ('category',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.SET_NULL,
                                   to='ticket.Category',
                                   verbose_name='Категория')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['category'],
            },
        ),
    ]