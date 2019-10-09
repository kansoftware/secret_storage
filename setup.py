from setuptools import setup, find_packages
from os.path import join, dirname
import kan_secret_storage as ss

setup(
    name='kan_secret_storage',
    version=ss.__version__,
    description="Python Secret Storage package",
    packages=["kan_secret_storage"],
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=['pycryptodome'],
    author="Andrew KAN",
    author_email="kan@kansoftware.ru",
    license="GPL-3",
    url="https://github.com/kansoftware/secret_storage",
)
