from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='zim_validate',
    version='0.0.2',
    description='A package to validate Zimbabwean Mobile numbers,passports,national IDs,drivers licenses etc',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/RONALD55/ZimPlaces-Python-Library',
    author='Ronald Nyasha Kanyepi',
    author_email='kanyepironald@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['zimbabwe', 'regex in Zimbabwe', 'validate Zimbabwean drivers license', 'validate Zimbabwean passports', 'validate Zimbabwean mobile numbers',
              'validate Zimbabwean national IDs'],
    packages=find_packages(),
    install_requires=[],


)
