from audit.middleware import current_user


def register(*models):
    """Call from AppConfig.ready() to connect audit signals to your models."""
    from django.db.models.signals import pre_save, post_save, post_delete

    for model in models:
        pre_save.connect(_pre_save, sender=model, weak=False)
        post_save.connect(_post_save, sender=model, weak=False)
        post_delete.connect(_post_delete, sender=model, weak=False)


# ---------------------------------------------------------------------------
# Signal handlers
# ---------------------------------------------------------------------------
def _pre_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._audit_old = sender.objects.get(pk=instance.pk)._get_field_data()
        except sender.DoesNotExist:
            instance._audit_old = {}
    else:
        instance._audit_old = None


def _post_save(sender, instance, created, **kwargs):
    from .models import AuditLog

    current = instance._get_field_data()

    if created:
        AuditLog.objects.create(
            user=current_user(),
            action=AuditLog.Action.CREATE,
            model_name=sender.__name__,
            object_id=str(instance.pk),
            data=current,
        )
    else:
        old = getattr(instance, "_audit_old", {}) or {}
        changed = {
            k: {"old": old[k], "new": current[k]}
            for k in current
            if k in old and old[k] != current[k]
        }
        if changed:
            AuditLog.objects.create(
                user=current_user(),
                action=AuditLog.Action.UPDATE,
                model_name=sender.__name__,
                object_id=str(instance.pk),
                data=changed,
            )


def _post_delete(sender, instance, **kwargs):
    from .models import AuditLog

    AuditLog.objects.create(
        user=current_user(),
        action=AuditLog.Action.DELETE,
        model_name=sender.__name__,
        object_id=str(instance.pk),
        data=instance._get_field_data(),
    )


# ---------------------------------------------------------------------------
# audit_event — for views / tasks
# ---------------------------------------------------------------------------


def audit_event(event, *, user=None, instance=None, data=None):
    from .models import AuditLog

    AuditLog.objects.create(
        user=user or current_user(),
        action=AuditLog.Action.CUSTOM,
        model_name=type(instance).__name__ if instance else "",
        object_id=str(instance.pk) if instance and instance.pk else None,
        event=event,
        data=data or {},
    )
