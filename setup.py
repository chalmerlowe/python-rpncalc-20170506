import subprocess
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class TestAndLint(TestCommand):

    description = 'run linters and tests'
    user_options = []

    def run_tests(self, *args, **kwargs):
        TestCommand.run_tests(self, *args, **kwargs)
        self._run(['flake8', 'rpncalculator', 'test', 'setup.py'])

    def _run(self, command):
        try:
            subprocess.check_call(command)
        except subprocess.CalledProcessError as error:
            print('Command failed with exit code', error.returncode)
            sys.exit(error.returncode)


setup(
    name='rpn-calc-engine',
    version='0.1.0',
    author='jeffrey k eliasen',
    author_email='jeff+rpn-calc-engine@jke.net',
    description='an RPN calculator engine for use in workshops',
    license='MIT',
    keywords='calculator',
    url='',
    packages=['rpncalculator'],
    long_description=open('README.md').read(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    install_requires=[
        'funcsigs',
    ],
    tests_require=[
        'nose',
        'mock',
    ],
    test_suite='nose.collector',
    cmdclass={
        'test': TestAndLint,
    },
)
