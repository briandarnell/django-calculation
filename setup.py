#!/usr/bin/env python
from setuptools import setup

setup(
    name="django-calculation",
    packages=["calculation"],
    include_package_data=True,
    version="0.0.8",
    description="A Django app to make simple calculations in your django forms",
    long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
    author="Blas Fernandez",
    author_email="blasferna@gmail.com",
    url="https://github.com/blasferna/django-calculation",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=["Django>=2.2"],
    python_requires=">=3.6",
)
