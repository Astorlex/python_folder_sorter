from setuptools import setup, find_packages


NAME = 'clean_folder'
VERSION = '1.0.1'
DESCRIPTION = 'Simple Folder Sorter'
AUTHOR = 'Oleksiy Storozhuk'
AUTHOR_EMAIL = 'astorlex@gmail.com'
URL = 'https://github.com/Astorlex/python_folder_sorter'

with open('./requirements.txt', 'r') as f:
    INSTALL_REQUIRES = list(filter(lambda l: bool(l.strip()), f.readlines()))

PACKAGES = find_packages()
PYTHON_REQUIRES = '>=3.11'

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12'
]

with open('README.md', 'r', encoding='utf-8') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=PACKAGES,
    python_requires = PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    entry_points={
    'console_scripts': [
        'clean-folder = clean_folder.clean:main',
    ]
}
)