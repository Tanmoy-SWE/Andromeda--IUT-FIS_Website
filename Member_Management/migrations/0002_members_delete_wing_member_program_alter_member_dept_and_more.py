# Generated by Django 4.0.1 on 2022-03-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member_Management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=100)),
                ('student_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Wing',
        ),
        migrations.AddField(
            model_name='member',
            name='program',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='dept',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
