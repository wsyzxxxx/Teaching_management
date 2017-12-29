# Generated by Django 2.1 on 2017-12-27 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20171227_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isread',
            name='read_announce',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.Announcement'),
        ),
        migrations.AlterField(
            model_name='isread',
            name='read_message',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.Message'),
        ),
    ]