import os
import sys
import unittest

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================
This version of Nosorog requires at least Python {}.{}, but
you're trying to install it on Python {}.{}. To resolve this,
consider upgrading to a supported Python version.
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

requires = [
]
test_requirements = [
]


def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='tests_*.py')
    return test_suite


about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "nosorog", "__version__.py"), mode="r", encoding="utf-8") as f:
    exec(f.read(), about)

with open("README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='security, protect, nosorog',
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"nosorog": "nosorog"},
    include_package_data=True,
    python_requires=">=3.7, <4",
    packages=['nosorog'],
    install_requires=[],
    license=about["__license__"],
    zip_safe=False,
    test_suite='setup.test_suite',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Topic :: Security',
        'Topic :: Software Development :: Libraries',
    ],
    project_urls={
        "Documentation": "https://nosorog.readthedocs.io",
        "Source": "https://github.com/vyacheslavlobanov/nosorog",
    },
)
