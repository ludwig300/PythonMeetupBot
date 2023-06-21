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
        max_length=30
    )
    firstname = models.CharField(
        verbose_name='Имя',
        blank=True,
        default='',
        max_length=20
    )
    lastname = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        default='',
        max_length=20
    )
    occupation = models.TextField(
        verbose_name='Чем занимаешься?',
        blank=True,
        default='',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(
        verbose_name='Название мероприятия',
        max_length=100
    )
    date = models.DateField(verbose_name='Дата мероприятия')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


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
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Доклад'
        verbose_name_plural = 'Доклады'

    def __str__(self):
        return self.title


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

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f"Question from {self.user.username} for report {self.report.title}"
