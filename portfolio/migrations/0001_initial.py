# Generated by Django 4.0.1 on 2022-01-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('posted_time', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['-posted_time'],
            },
        ),
    ]
