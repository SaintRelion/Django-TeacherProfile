from decimal import Decimal

from django.db import models

# Fields never included in the JSON snapshot
DEFAULT_IGNORE = {"created_at", "updated_at", "modified", "created", "modified_at"}


class AuditMixin(models.Model):

    ignore_fields = []  # override per model

    class Meta:
        abstract = True

    def _get_field_data(self):
        ignore = DEFAULT_IGNORE | set(self.ignore_fields)
        data = {}
        for field in self._meta.concrete_fields:
            if field.name in ignore:
                continue
            val = getattr(self, field.attname)
            if hasattr(val, "pk"):
                val = val.pk
            elif hasattr(val, "isoformat"):
                val = val.isoformat()
            elif isinstance(val, Decimal):
                val = float(val)
            data[field.attname] = val
        return data
