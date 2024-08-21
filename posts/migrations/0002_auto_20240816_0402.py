# Generated by Django 5.1 on 2024-08-16 04:02
from django.db import migrations, transaction

def populate_status(apps, schema_editor):
    Status = apps.get_model("posts", "Status")
    
    with transaction.atomic():
        Status.objects.create(name="published", description="A post available for all to view")
        Status.objects.create(name="draft", description="A post only visible to the author")
        Status.objects.create(name="archived", description="An older post, visible to logged in users")

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status),
    ]
