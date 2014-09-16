from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-tasks',
    version='0.1',
    url='http://github.com/frascoweb/frasco-tasks',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Celery integration for Frasco",
    long_description=desc(),
    py_modules=['frasco_tasks'],
    platforms='any',
    install_requires=[
        'frasco',
        'celery==3.1.13[redis]'
    ]
)