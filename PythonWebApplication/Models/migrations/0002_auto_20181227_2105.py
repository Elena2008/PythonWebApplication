# Generated by Django 2.1.4 on 2018-12-27 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_ban', models.DateTimeField()),
            ],
            options={
                'ordering': ['-date_of_ban'],
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.IntegerField(blank=True, choices=[(1, 'Voronezh'), (2, 'Moscow'), (3, 'St. Petersburg'), (4, 'Novgorod')], default=1, help_text='Выберите город'),
        ),
        migrations.AddField(
            model_name='ban',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ban',
            name='employer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employer', to=settings.AUTH_USER_MODEL),
        ),
    ]
