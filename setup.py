from setuptools import setup, find_packages
from src import version

setup(
    name = "ynspector",
    version = version,
    packages = ["ynspector"],
    package_dir = {"ynspector": "src"},
    author = "Guilherme Chapiewski",
    author_email = "guilherme.chapiewski@gmail.com",
    description = "ynspector inspects a given directory and runs a command everytime a file is changed.",
    license = "Apache License 2.0",
    keywords = "tool testing directory",
    url = "http://guilhermechapiewski.github.com/ynspector/",
    long_description = "ynspector inspects a given directory and runs a command everytime a file is changed.",
    
    # generate script automatically
    entry_points = {
        'console_scripts': [
            'ynspect = ynspector:run',
        ],
    },

)
