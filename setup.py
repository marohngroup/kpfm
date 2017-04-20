# -*- coding: utf-8 -*-
import sys
import io

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = 'kpfm/_version.py'
versioneer.versionfile_build = 'kpfm/_version.py'
versioneer.tag_prefix = ''  # tags are like 1.2.0
versioneer.parentdir_prefix = 'kpfm-'  # dirname like 'myproject-1.2.0'

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Please install or upgrade setuptools or pip")
    sys.exit(1)

readme = io.open('README.rst', mode='r', encoding='utf-8').read()
doclink = """
Documentation
-------------

The full documentation is at http://kpfm.rtfd.org."""
history = io.open('HISTORY.rst', mode='r',
                  encoding='utf-8').read().replace('.. :changelog:', '')

# Use cmdclass.update to add additional commands as necessary. See
# https://docs.python.org/2/distutils/extending.html#integrating-new-commands
cmdclass = versioneer.get_cmdclass()

setup(
    name='kpfm',
    version=versioneer.get_version(),
    description='Kelvin Probe Force Microscopy (KPFM) signal processing utilities.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    license='MIT',
    author='Ryan Dwyer',
    author_email='ryanpdwyer@gmail.com',
    url='https://github.com/ryanpdwyer/kpfm',
    zip_safe=False,
    include_package_data=True,
    # This lets setuptools include_package_data work with git
    setup_requires=["setuptools_git >= 0.3"],
    packages=find_packages(),

    # Add requirements here. If the requirement is difficult to install,
    # add to docs/conf.py MAGIC_MOCK and .travis.yml 'conda install ...'
    # instead of here
    # For example, numpy, scipy, matplotlib, pandas are there instead
    install_requires=["decorator", "six", "sigutils", "munch", "decorator",
                      "tqdm"],

    tests_require=['nose'],
    test_suite='nose.collector',
    cmdclass=cmdclass,
    keywords='kpfm',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
