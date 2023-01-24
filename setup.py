import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='timer',
    version='0.0.1',
    author='Melih Unsal',
    author_email='melih@synthdata.co',
    description='Timer Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/melih1996/timer.git',
    license='MIT',
    packages=['timer'],
    install_requires=[],
)