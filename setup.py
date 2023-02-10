from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='me',
    version='2.85',
    packages=find_packages(),
    url='https://14wual.github.io/me',
    license='MIT License',
    author='Carlos Padilla',
    author_email='cpadlab@gmail.com',
    description='Me is an application that allows you to perform certain basic tasks. Manage passwords, contacts, tasks, notes, search the web with a command, emulate python, among others!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'configparser',
        'cmd',
        'datetime',
        'argparse',
        'sys',
        'os',
        'pycryptools',
        'getpass',
        'subprocess',
        'webbrowser',
        'csv',
        'pyperclip',
        'urllib',
        'sqlite3',
        'signal',
        'psutil',
        'socket',
        'smtplib'
        ],
    project_urls={
        "Source Code": "https://github.com/14wual/me/",
        "Bug Tracker": "https://github.com/14wual/me/issues",
        "Documentation": "https://github.com/14wual/me/wiki",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],    
)
