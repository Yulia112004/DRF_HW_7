import re
from collections import OrderedDict

from rest_framework.exceptions import ValidationError


class LinkToVideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value: OrderedDict) -> None:

        pattern = r'https://www.youtube.com/.*'
        tmp_val = dict(value).get(self.field)

        if not bool(re.search(pattern, tmp_val)):
            raise ValidationError('Ссылка не должна вести на сторонние ресурсы, кроме youtube.com.')