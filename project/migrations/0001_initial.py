# Generated by Django 2.0 on 2020-03-16 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='project_comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=800)),
                ('target', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateTimeField()),
                ('rating', models.IntegerField()),
                ('reports', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Project_pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgage_url', models.TextField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project_data')),
            ],
        ),
        migrations.CreateModel(
            name='project_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project_data')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='project_tags',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Tag'),
        ),
        migrations.AddField(
            model_name='project_comments',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project_data'),
        ),
    ]