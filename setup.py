from setuptools import setup, find_packages

setup(
    name='prototype',
    version='0.0.1',
    author='Guillermo Adrián Molina',
    author_email='guillermoadrianmolina@hotmail.com',
    description='Interpreter of the Prototype language. ',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires = [ 'setuptools-git' ],
    include_package_data = True,
    packages=find_packages(),
    entry_points = {
        'console_scripts' : [ 'prototype = prototype.prototypeapp:main']
    },
    test_suite = 'prototype.run_tests.get_suite',

)
