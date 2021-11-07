# Generated by mysite 3.2.8 on 2021-10-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_desc', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
