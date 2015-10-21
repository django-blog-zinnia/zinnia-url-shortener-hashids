"""Setup script of zinnia-url-shortener-hashids"""
from setuptools import setup
from setuptools import find_packages

setup(
    name='zinnia-url-shortener-hashids',
    version='1.1',

    description='Hashids URL shortener backend for django-blog-zinnia',
    long_description=open('README.rst').read(),
    keywords='django, zinnia, url, hashids',

    author='Fantomas42',
    author_email='fantomas42@gmail.com',
    url='https://github.com/Fantomas42/zinnia-url-shortener-hashids',

    packages=find_packages(exclude=['demo_zinnia_hashids']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license='BSD License',
    include_package_data=True,
    zip_safe=False,
    install_requires=['hashids']
)
