from setuptools import setup, find_packages
#import py2exe


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='guicodebuilder',
    version='1.2.0',
    description='Custom GUI class code generator',
    long_description=readme(),

    author='Christopher Maue',
    author_email='csmaue@gmail.com',
    license='GNUv2',
    url='https://github.com/csm0042/guicodebuilder.git',

    packages=['guicodebuilder'],
    include_package_data=True,

    scripts=['scripts/create_custom_gui_class.py'],
    console=['scripts/create_custom_gui_class.py'],
    #windows=['scripts/main.py'],

    #options={'py2exe': {'bundle_files': 2, 'compressed': True}},
    zip_safe=False,

    #data_files=['gui_setup.ini']
    )