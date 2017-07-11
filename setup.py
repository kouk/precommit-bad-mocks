#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="bad-mocks",
    version='1.0',

    description="Find bad mock methods in tests",
    packages=setuptools.find_packages(where='src'),
    zip_safe=True,
    package_dir={"": "src"},

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'bad-mocks = bad_mocks:main',
        ]
    },
)
