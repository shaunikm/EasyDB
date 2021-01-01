import setuptools

setuptools.setup(
    name='EasyDatabase',
    version='2.1',
    author='Shaunik Musukula',
    author_email='shaunik.musukula@gmail.com',
    description='A database that is very easy to set up and use',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shaunikm/EasyDB',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
