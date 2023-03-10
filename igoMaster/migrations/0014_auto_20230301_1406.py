# Generated by Django 3.2.12 on 2023-03-01 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igoMaster', '0013_alter_user_joinedat'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='favoris',
            name='etablishment',
        ),
        migrations.AddField(
            model_name='banner',
            name='name',
            field=models.CharField(default='sans nom', max_length=500),
        ),
        migrations.AddField(
            model_name='favoris',
            name='etablishments',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='favoris',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='igoMaster.user'),
        ),
    ]
