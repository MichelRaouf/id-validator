# Generated by Django 4.2.19 on 2025-03-02 17:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('id_validator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='APICallLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('response_status', models.IntegerField()),
                ('api_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_calls', to='id_validator.nationalidapikey')),
            ],
        ),
    ]
