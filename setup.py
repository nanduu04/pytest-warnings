# encoding: utf-8

from setuptools import setup


setup(name="pytest-warnings",
      version='0.0.1',
      author='Nandu Pokhrel',
      author_email='nandupokhrel@gmail.com',
      description='pytest plugin to capture all all the warnings and put them in txt file',
      long_description=open("README.md").read(),
      long_description_content_type='text/markdown',
      license="MIT",
      packages=['pytest_capture_deprecatedwarnings'],
      entry_points={'pytest11': ['pytest-warnings']},
      install_requires=['pytest', 'importlib_metadata'],
      )