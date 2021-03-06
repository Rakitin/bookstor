# Generated by Django 3.2.13 on 2022-05-10 15:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга'},
        ),
        migrations.AlterModelOptions(
            name='catigory',
            options={'verbose_name': 'Категория'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Catigory',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='main.Author', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='book',
            name='catigory',
            field=models.ManyToManyField(to='main.Catigory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='catigory',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
