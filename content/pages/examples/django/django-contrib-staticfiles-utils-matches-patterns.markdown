title: django.contrib.staticfiles.utils matches_patterns Example Code
category: page
slug: django-contrib-staticfiles-utils-matches-patterns-examples
sortorder: 500011077
toc: False
sidebartitle: django.contrib.staticfiles.utils matches_patterns
meta: Python example code for the matches_patterns callable from the django.contrib.staticfiles.utils module of the Django project.


matches_patterns is a callable within the django.contrib.staticfiles.utils module of the Django project.


## Example 1 from django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE.txt)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-pipeline / pipeline / storage.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./storage.py)

```python
# storage.py
import gzip

from io import BytesIO

from django.contrib.staticfiles.storage import CachedStaticFilesStorage, ManifestStaticFilesStorage, StaticFilesStorage
~~from django.contrib.staticfiles.utils import matches_patterns

from django.core.files.base import File


class PipelineMixin(object):
    packing = True

    def post_process(self, paths, dry_run=False, **options):
        if dry_run:
            return

        from pipeline.packager import Packager
        packager = Packager(storage=self)
        for package_name in packager.packages['css']:
            package = packager.package_for('css', package_name)
            output_file = package.output_filename
            if self.packing:
                packager.pack_stylesheets(package)
            paths[output_file] = (self, output_file)
            yield output_file, output_file, True
        for package_name in packager.packages['js']:
            package = packager.package_for('js', package_name)
            output_file = package.output_filename
            if self.packing:


## ... source file abbreviated to get to matches_patterns examples ...



class GZIPMixin(object):
    gzip_patterns = ("*.css", "*.js")

    def _compress(self, original_file):
        content = BytesIO()
        gzip_file = gzip.GzipFile(mode='wb', fileobj=content)
        gzip_file.write(original_file.read())
        gzip_file.close()
        content.seek(0)
        return File(content)

    def post_process(self, paths, dry_run=False, **options):
        super_class = super(GZIPMixin, self)
        if hasattr(super_class, 'post_process'):
            for name, hashed_name, processed in super_class.post_process(paths.copy(), dry_run, **options):
                if hashed_name != name:
                    paths[hashed_name] = (self, hashed_name)
                yield name, hashed_name, processed

        if dry_run:
            return

        for path in paths:
            if path:
~~                if not matches_patterns(path, self.gzip_patterns):
                    continue
                original_file = self.open(path)
                gzipped_path = f"{path}.gz"
                if self.exists(gzipped_path):
                    self.delete(gzipped_path)
                gzipped_file = self._compress(original_file)
                gzipped_path = self.save(gzipped_path, gzipped_file)
                yield gzipped_path, gzipped_path, True


class NonPackagingMixin(object):
    packing = False


class PipelineStorage(PipelineMixin, StaticFilesStorage):
    pass


class NonPackagingPipelineStorage(NonPackagingMixin, PipelineStorage):
    pass


class PipelineCachedStorage(PipelineMixin, CachedStaticFilesStorage):
    pass


## ... source file continues with no further matches_patterns examples...

```

