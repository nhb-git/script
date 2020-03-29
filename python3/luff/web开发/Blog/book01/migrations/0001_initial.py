# Generated by Django 2.0.5 on 2020-03-22 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('telephone', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=128)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('authors', models.ManyToManyField(to='book01.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book01.Publish'),
        ),
        migrations.AddField(
            model_name='author',
            name='author_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book01.AuthorDetail'),
        ),
    ]
