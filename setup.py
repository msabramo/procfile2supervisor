import os
import sys
from setuptools import setup

this_dir = os.path.dirname(__file__)
long_description = "\n" + open(os.path.join(this_dir, 'README.rst')).read()

setup(
    name='procfile2supervisor',
    version='0.0.0',
    description='Creates a supervisor config from a Procfile',
    long_description=long_description,
    keywords='Procfile,supervisor,supervisord',
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    url='https://github.com/msabramo/procfile2supervisor',
    packages=['procfile2supervisor'],
    zip_safe=False,
    install_requires=['click', 'honcho[export]'],
    entry_points = """\
      [console_scripts]
      procfile2supervisor = procfile2supervisor.cli:main
    """,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
