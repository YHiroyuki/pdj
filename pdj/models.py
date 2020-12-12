from django.db.models import fields, Field

class BigAutoField(fields.AutoField):
    def db_type(self, connection):
        if 'mysql' in connection.__class__.__module__:
            return 'bigint AUTO_INCREMENT'
        return super(BigAutoField, self).db_type(connection)


class EnumField(Field):
    def __init__(self, *args, **kwargs):
        super(EnumField, self).__init__(*args, **kwargs)
        assert self.choices, "Need choices for enumeration"

    def db_type(self, connection):
        if not all(isinstance(col, str) for col, _ in self.choices):
            raise ValueError("MySQL ENUM values should be str")
        return "ENUM({})".format(','.join("'{}'".format(col) for col, _ in self.choices))
