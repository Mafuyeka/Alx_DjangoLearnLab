# Generated by Django 4.2.23 on 2025-07-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'permissions': [('can_view', 'Can view article'), ('can_create', 'Can create article'), ('can_edit', 'Can edit article'), ('can_delete', 'Can delete article')],
            },
        ),
    ]
