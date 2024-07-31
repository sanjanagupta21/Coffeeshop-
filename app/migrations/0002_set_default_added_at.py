from django.db import migrations, models
import django.utils.timezone

def set_default_added_at(apps, schema_editor):
    CartItem = apps.get_model('app', 'CartItem')
    default_time = django.utils.timezone.now()
    for item in CartItem.objects.all():
        if not item.added_at:
            item.added_at = default_time
            item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.RunPython(set_default_added_at),
    ]
