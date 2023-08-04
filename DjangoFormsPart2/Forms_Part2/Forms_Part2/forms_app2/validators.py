from django.core.exceptions import ValidationError


def validate_text(value):
    if '_' in value:
        raise ValidationError('"_" is not valid character')


def validate_priority(value):
    if value < 1 or value > 10:
        raise ValidationError('number must be between 1 and 10')


class ValidateInRange:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or value > self.max_value:
            raise ValidationError(f'number must be between {self.min_value} and {self.max_value}')
