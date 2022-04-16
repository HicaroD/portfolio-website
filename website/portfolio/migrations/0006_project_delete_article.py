# Generated by Django 4.0.3 on 2022-04-16 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('technologies', models.TextField(null=True)),
                ('project_link', models.CharField(max_length=100, null=True)),
                ('rating', models.SmallIntegerField()),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]