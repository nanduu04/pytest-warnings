
from setuptools import setup

setup(name="pytest_capture_warnings",
      version='0.0.1',
      author='Nandu Pokhrel',
      author_email='nandupokhrel@gmail.com',
      version="0.0.3",
      url="https://github.com/athinkingape/pytest-capture-warnings",
      description="pytest plugin to capture all warnings and put them in one file of your choice",
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      license="MIT",
      packages=["pytest_capture_warnings"],
      entry_points={"pytest11": ["pytest_capture_warnings = pytest_capture_warnings"]},
      install_requires=["pytest", "importlib_metadata"],
)
