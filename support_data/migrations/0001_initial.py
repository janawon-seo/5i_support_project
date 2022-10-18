# Generated by Django 4.1.2 on 2022-10-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('people_num', models.CharField(max_length=128)),
                ('input_num', models.CharField(max_length=128)),
                ('is_approval', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'support',
            },
        ),
    ]
