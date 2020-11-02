# Generated by Django 3.1.2 on 2020-11-02 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import web.apps.commons.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMultipleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('image', models.ImageField(upload_to=web.apps.commons.utils.RandomFileName('upload/user_multiple_img'))),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermultipleimages_created_user', to=settings.AUTH_USER_MODEL, verbose_name='Created User')),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermultipleimages_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='Updated User')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiple_image', to='user_profile.userprofile')),
            ],
            options={
                'verbose_name': 'User Multiple Image',
                'verbose_name_plural': 'User Multiple Images',
            },
        ),
    ]
