from setuptools import setup, find_packages

setup(
    name='test-package-1337',
    version='0.1',
    packages=find_packages(),
    description='This is a awesome test project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='David B',
    author_email='david.bacelj@gmail.com',
    url='https://github.com/yourusername/your_package_name',
    install_requires=[
        'numpy',
        'pandas>=1.0.0',
        'matplotlib<=3.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)