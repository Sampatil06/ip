# Generated by Django 4.1.2 on 2023-10-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Digital_library', '0006_alter_books_book_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Author_name', models.CharField(default=None, max_length=50)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]