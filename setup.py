from setuptools import setup
import os

import spikesortingvalidation

install_requires = [
                    'numpy',
                    'scipy',
                    ]

long_description = ""

setup(
    name = "spikesortingvalidation",
    version = spikesortingvalidation.__version__,
    packages = ['spikesortingvalidation', ],
    install_requires=install_requires,
    author = "P. Yger, S.Garcia",
    author_email = "",
    description = "Collection of tools for validation of spike sorting algorithms",
    long_description = long_description,
    license = "MIT",
    url='https://github.com/spike-sorting-validation/spikesortingvalidation',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering']
)
