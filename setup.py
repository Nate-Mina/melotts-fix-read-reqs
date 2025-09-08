import os
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

# Read requirements.txt directly to avoid importing pip internals which
# aren't available in PEP 517 isolated build subprocesses.
def _read_requirements(path):
    reqs = []
    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            reqs.append(line)
    return reqs

cwd = os.path.dirname(os.path.abspath(__file__))
reqs = _read_requirements(os.path.join(cwd, 'requirements.txt'))
class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        os.system('python -m unidic download')


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        os.system('python -m unidic download')

setup(
    name='melotts',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    package_data={
        '': ['*.txt', 'cmudict_*'],
    },
    entry_points={
        "console_scripts": [
            "melotts = melo.main:main",
            "melo = melo.main:main",
            "melo-ui = melo.app:main",
        ],
    },
)
