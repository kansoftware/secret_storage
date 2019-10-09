from setuptools import setup, find_packages
from os.path import join, dirname
import secret_storage

setup(
    name='secret_storage',
    version=secret_storage.__version__,
    description="Python Secret Storage package",
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author="Andrew KAN",
    author_email="kan@kansoftware.ru",
    license="GPL-3",
    url="https://github.com/kansoftware/secret_storage",
)
