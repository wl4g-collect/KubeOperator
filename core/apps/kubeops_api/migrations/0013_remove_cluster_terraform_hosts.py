# Generated by Django 2.1.2 on 2019-09-18 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0012_auto_20190917_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster',
            name='terraform_hosts',
        ),
    ]