#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    
]

setup(
    author="Moshe Dicker",
    author_email='dickermoshe@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="A small python package for detecting nsfw on a Windows display.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords='nsfw_screen_detect',
    name='nsfw_screen_detect',
    packages=find_packages(include=['nsfw_screen_detect', 'nsfw_screen_detect.*']),
    url='https://github.com/dickermoshe/nsfw_screen_detect',
    version='0.1.0',
    zip_safe=False,
)
