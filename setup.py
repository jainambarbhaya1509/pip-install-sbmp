from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='sbmp',
  version='1.0.0',
  description='SBMP',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Jainam Barbhaya',
  author_email='jainambarbhaya1509@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['sbmp'], 
  packages=find_packages(),
)