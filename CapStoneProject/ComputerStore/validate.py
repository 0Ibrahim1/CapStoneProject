from django.core.exceptions import ValidationError

def check_file_size_10mb(value):
    #size in byte
    limit = 10 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size cannot exceed 10 MB.')