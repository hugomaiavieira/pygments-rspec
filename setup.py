#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-rspec',
    version='0.1',
    description='Pygments lexer for Ruby + RSpec.',
    long_description=open('README.rst').read(),
    keywords='pygments ruby rspec lexer',
    license='BSD',

    author='Hugo Maia Vieira',
    author_email='hugomaiavieira@gmail.com',

    url='https://github.com/hugomaiavieira/pygments-rspec',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.lexers]
                    rspec=pygments_rspec:RspecLexer''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)