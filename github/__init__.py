import sys
import importlib.abc
import importlib.machinery

from .ghprocessor import get_github, create_base_url


def is_package(fullname):
    return get_github(create_base_url(fullname)+'.py') is None


class GithubModuleFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, name, path, target=None):
        print('MyModuleFinder: Trying to load: {}'.format(name))

        if not name.startswith('github.'):
            return None
        return importlib.machinery.ModuleSpec(name, GithubLoader(), is_package=is_package(name))


class GithubLoader(importlib.abc.SourceLoader):
    def get_filename(self, fullname):
        print('MyLoader: Requesting filename for {}'.format(fullname))
        base_url = create_base_url(fullname)
        if is_package(fullname):
            return base_url+'/__init__.py'
        return base_url+'.py'

    def get_data(self, filename):
        print('MyLoader: Fetching {} from our virtual filesystem'.format(filename))
        if filename == 'http://github.com/FAKE/__init__.py':
            return ''
        return get_github(filename)


# Install module
sys.meta_path.insert(0, GithubModuleFinder())
