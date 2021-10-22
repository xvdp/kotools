"""@xvdp
"""
import os.path as osp
from setuptools import setup, find_packages

def _path(*args):
    return osp.join(osp.split(__file__)[0], *args)

def _readme():
    with open(_path('README.md')) as _fo:
        return _fo.read()

def _requirements():
    with open(_path('requirements.txt')) as _fo:
        return _fo.read().split()

def _set_version(version):
    with open(_path('koreto','version.py'), 'w') as _fi:
        _fi.write('"""@xvdp generated by setup.py"""\n')
        _fi.write("__version__='"+version+"'\n")
    return version

def build_packages():
    """ setup """
    setup(
        name='koreto',
        version=_set_version("0.0.6"),
        author="xvdp",
        url='https://github.com/xvdp/koreto',
        license='MIT',
        description='koreto, spome common learning tools',
        long_description=_readme(),
        install_requires=_requirements(),
        packages=find_packages(),
        tests_require=["pytest"],
        include_package_data=True,
        python_requires='>=3.6',
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
    )

if __name__ == '__main__':
    build_packages()
