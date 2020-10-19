
#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import os
setup(
    author="Max Bertolero",
    author_email='mbertolero@me.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    download_url = 'https://github.com/mb3152/abcd_dl/archive/master.zip',
    description="ABCD Downloader",
    license="GNU General Public License v3",
    include_package_data=True,
    keywords='abcd',
    name='abcd',
    version='0.1.0',
    zip_safe=False,
)