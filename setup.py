from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name="redis-sync",
    version=version,
    description='Redis sync tool that public cloud',
    url='https://github.com/cctv86/redis-sync',
    license='MIT',
    author='zhigang.hong',
    author_email='627849521@qq.com',
    packages=find_packages(),
    py_modules=['redis-sync'],
    install_requires=['redis >= 3.5.1',],
    include_package_data=True,
    zip_safe=True,
)
