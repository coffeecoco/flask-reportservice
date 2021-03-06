import os
from setuptools import find_packages, setup

# Load README file for long description.
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path.
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Main setup and configuration.
setup(
    name='flask-reportservice',
    version='0.8.1',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License Version 2.0',
    description='A Flask service to export PDF and XML reports.',
    long_description=README,
    url='https://github.com/mbp76/flask-reportservice',
    author='mbp76',
    author_email='mbp76@users.noreply.github.com',
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'psycopg2',
        'pdfkit',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pypdf2',
        'pytest-cov',
        'pytest', # Keep at the end to avoid conflicts.
    ],
)
