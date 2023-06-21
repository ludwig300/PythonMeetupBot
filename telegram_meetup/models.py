from django.db import models


class User(models.Model):
    ROLES_CHOICES = [
        ('Organizer', 'Организатор'),
        ('Speaker', 'Докладчик'),
        ('User', 'Пользователь'),
    ]
    role = models.CharField(
        verbose_name='Роль',
        choices=ROLES_CHOICES,
        default='User',
        max_length=10
    )
    username = models.CharField(
        verbose_name='Username в Telegram',
        unique=True,
        db_index=True,
    )
    firstname = models.CharField(
        verbose_name='Имя',
        blank=True,
        default='',
    )
    lastname = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        default='',
    )
    occupation = models.TextField(
        verbose_name='Чем занимаешься?',
        blank=True,
        default='',
    )


class Event(models.Model):
    title = models.CharField(
        verbose_name='Название мероприятия',
        max_length=100
    )
    date = models.DateField(verbose_name='Дата мероприятия')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Report(models.Model):
    title = models.CharField(
        verbose_name='Название доклада',
        max_length=100
    )
    speaker = models.ForeignKey(
        User,
        related_name='reports',
        verbose_name='Докладчик',
        on_delete=models.CASCADE
    )
    description = models.TextField(
        verbose_name='Кратко о теме доклада'
    )
    datetime = models.DateTimeField(verbose_name='Время выступления')
    event = models.ForeignKey(
        Event, related_name='reports',
        verbose_name='Мероприятие',
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    user = models.ForeignKey(
        User,
        related_name='questions',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    question = models.TextField(verbose_name='Вопрос')
    report = models.ForeignKey(
        Report,
        related_name='questions',
        verbose_name='Название доклада',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
