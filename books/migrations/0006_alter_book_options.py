# Generated by Django 4.0.3 on 2022-04-07 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
