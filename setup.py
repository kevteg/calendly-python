from setuptools import setup
import sys
import os


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='calendly',
    version='1',
    description="A Python wrapper for the Calendly API  (https://developer.calendly.com/docs/)",
    long_description=readme(),
    classifiers=[
        'License :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='Calendly python api',
    url='https://github.com/kevteg/calendly-python',
    author='kevteg',
    author_email='kevteg05@gmail.com',
    license='MIT',
    packages=[
        'calendly_client',
    ],
    install_requires=[
        'requests'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=False
)