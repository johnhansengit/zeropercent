from django.contrib.staticfiles.storage import StaticFilesStorage
from django.utils.encoding import filepath_to_uri
import os
import time

class CustomStaticFilesStorage(StaticFilesStorage):
    def url(self, name):
        url = super().url(name)
        if name.endswith('.css') or name.endswith('.js'):
            path = self.path(name)
            timestamp = int(os.stat(path).st_mtime)
            url = f"{url}?v={timestamp}"
        return url
