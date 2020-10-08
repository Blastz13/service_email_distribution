# Generated by Django 3.1 on 2020-10-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_distribution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageThankYou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=7, unique=True, verbose_name='Гео')),
                ('html_page', models.FileField(upload_to='uploads/templates/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Страница спасибо',
                'verbose_name_plural': 'Страницы спасибо',
            },
        ),
        migrations.AlterModelOptions(
            name='emailsubscriber',
            options={'verbose_name': 'Подписчик по почте', 'verbose_name_plural': 'Подписчики по почте'},
        ),
    ]
