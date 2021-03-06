# Generated by Django 4.0.4 on 2022-04-12 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('google_trends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=250)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=250, null=True)),
                ('snippet', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('image_url', models.CharField(blank=True, max_length=250, null=True)),
                ('language', models.CharField(blank=True, max_length=250, null=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=250, null=True)),
                ('types', models.CharField(blank=True, max_length=250, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('trend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='google_trends.trend')),
            ],
        ),
    ]
