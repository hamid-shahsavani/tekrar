from setuptools import setup , find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = "tekrar",
  version = "0.1.0",
  description = "create loading animation in python cli project ...",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = "SYS113",
  author_email = "051.SYS113@gmail.com",
  url = "https://github.com/sys113/tekrar",
  keywords = ["tekrar", "wait", "loading"],
  packages = find_packages(),
  install_requires=['cursor'],
  classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: Implementation",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
)
