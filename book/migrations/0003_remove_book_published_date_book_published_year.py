# Generated by Django 5.1.6 on 2025-03-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_description_book_language_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
