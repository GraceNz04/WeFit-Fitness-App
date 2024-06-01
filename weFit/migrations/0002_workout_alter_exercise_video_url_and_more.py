# Generated by Django 4.2.13 on 2024-05-31 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weFit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='exercise',
            name='video_url',
            field=models.FileField(upload_to='weFit/uploads'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weFit.workout'),
        ),
    ]