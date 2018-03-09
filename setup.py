from distutils.core import setup

setup(
    name='Jammin',
    version='1.0',
    author='',
    author_email='',
    license='',
    packages=['src'],
    scripts=['bin/jammin.exe'],
    install_requires=[
        'nltk', 'tweepy'
    ]
)
