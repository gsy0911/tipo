import setuptools
import os


def get_version(init_file_path):
    version_line = list(
        filter(lambda l: l.startswith('VERSION'), open(init_file_path))
    )[0]

    # eval is required to convert from string to tuple,
    # because VERSION defined in __init__.py is tuple
    version_tuple = eval(version_line.split('=')[-1])

    # join with dot
    return ".".join(map(str, version_tuple))


# get __version__ from __init__.py
init = os.path.join(
    os.path.dirname(__file__), 'tipo', '__init__.py'
)
VERSION = get_version(init_file_path=init)

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="tipo",
    version=VERSION,
    author="gsy0911",
    author_email="yoshiki0911@gmail.com",
    description="TIPO Is to Point Out your violation of PEP8",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gsy0911/tipo",
    packages=setuptools.find_packages(),
    install_requires=[
        "click"
    ],
    license="MIT",
    entry_points={
        'console_scripts': [
            'tipo = tipo.cli:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
    keywords=["keyword", "here"]
)
