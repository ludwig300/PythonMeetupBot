# Generated by Django 3.2.19 on 2023-06-23 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название мероприятия')),
                ('date', models.DateField(verbose_name='Дата мероприятия')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Organizer', 'Организатор'), ('Speaker', 'Докладчик'), ('User', 'Пользователь')], default='User', max_length=10, verbose_name='Роль')),
                ('username', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='Username в Telegram')),
                ('chat_id', models.IntegerField(unique=True, verbose_name='ID чата в Telegram')),
                ('firstname', models.CharField(blank=True, default='', max_length=20, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, default='', max_length=20, verbose_name='Фамилия')),
                ('occupation', models.TextField(blank=True, default='', verbose_name='Чем занимаешься?')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название доклада')),
                ('description', models.TextField(verbose_name='Кратко о теме доклада')),
                ('datetime', models.DateTimeField(verbose_name='Время выступления')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='telegram_meetup.event', verbose_name='Мероприятие')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='telegram_meetup.user', verbose_name='Докладчик')),
            ],
            options={
                'verbose_name': 'Доклад',
                'verbose_name_plural': 'Доклады',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='telegram_meetup.report', verbose_name='Название доклада')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='telegram_meetup.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
