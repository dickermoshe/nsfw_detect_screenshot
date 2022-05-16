#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

requirements = [
    'wheel',
    'tensorflow',
    'numpy',
    'opencv-python',
    'Pillow',
    'mss',
    'pywinauto'
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
    long_description=long_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
    keywords='nsfw_screen_detect',
    name='nsfw_screen_detect',
    package_dir = {"": "src"},
    packages=find_packages(where="src"),
    url='https://github.com/dickermoshe/nsfw_detect_screenshot',
    version='0.2.1',
    zip_safe=False,

)
