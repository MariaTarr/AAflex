#from distutils.core import setup
from setuptools import setup, find_packages

setup(name='Esteno',
    version='1.0',
    description='Flexibility score for residue sin a protein',
    author='Alejandro Madrid, Xavier Soler, Maria Tarradas',
    author_email='maria.tarradas01@estudiant.upf.edu',
    url='https://github.com/MariaTarr/AAflex.git',
    keywords='flexibility',
    packages=find_packages(),
    install_requires=[
    'biopython',
    'pandas',
    'requests',
    'numpy',
    'matplotlib',
    'Pillow'
    ],
    entry_points = {
        'console_scripts': [
            'Esteno = modules.cmd_esteno:cmd_run',
            'RunEsteno = modules.gui_esteno:inf_run'
        ]
    },
    include_package_data=True,
    package_data={'images': ['*.png']},
)
