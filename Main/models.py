from django.db import models

######################################################################################################################


class Tag(models.Model):
    title = models.CharField(
        verbose_name='Название тематики',
        max_length=64,
        default='',
    )

    def __str__(self):
        return '{0}'.format(self.title)

    class Meta:
        ordering = 'title',
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'
        managed = True


######################################################################################################################


class Author(models.Model):
    name = models.CharField(
        verbose_name='ФИО автора',
        max_length=256,
        default='',
    )

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        ordering = 'name',
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        managed = True


######################################################################################################################


class Quote(models.Model):
    author = models.ForeignKey(
        Author,
        verbose_name='Автор цитаты',
        null=True,
        blank=True,
        default=None,
        related_name='Author',
        on_delete=models.CASCADE,
    )
    quote = models.TextField(
        blank=True,
    )
    create_date = models.DateTimeField(
        verbose_name='Дата добавления цитаты',
        auto_now_add=True,
        null=True,
    )

    def __str__(self):
        return '{0}. {1}...'.format(self.author, self.quote[:40])

    class Meta:
        ordering = 'author', 'create_date',
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
        managed = True

######################################################################################################################


class QuoteTag(models.Model):
    quote = models.ForeignKey(
        Quote,
        verbose_name='Цитата',
        null=True,
        blank=True,
        default=None,
        related_name='QuoteTag',
        on_delete=models.CASCADE,
    )
    tag = models.ForeignKey(
        Tag,
        verbose_name='Тематика',
        null=True,
        blank=True,
        default=None,
        related_name='TagQuote',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{0}. {1}'.format(self.tag, self.quote)

    class Meta:
        ordering = 'tag', 'quote',
        verbose_name = 'Тематика цитаты'
        verbose_name_plural = 'Тематики цитат'
        managed = True


######################################################################################################################
