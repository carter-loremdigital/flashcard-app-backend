# Generated by Django 5.1.6 on 2025-02-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='deck',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
