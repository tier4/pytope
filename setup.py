from setuptools import setup


setup(name='pytope',
      version='0.0.1',
      description='Polytope operations --- minimal functionality',
      url='https://github.com/heirung/pytope',
      author='Tor Aksel N. Heirung',
      author_email='github@heirung.com',
      license='MIT',
      packages=['pytope'],
      install_requires=[
        'numpy',
      ],
      zip_safe=False)