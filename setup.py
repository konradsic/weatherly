from setuptools import setup
import re

version = None
with open('weatherly/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.rst', encoding='utf-8') as readme_file: 
    readme = readme_file.read()


requirements = []
with open('requirements.txt') as requirements_file: 
    requirements = requirements_file.read().splitlines()

extras_require = {
    'docs': [
        'sphinx==5.3.0',
        'sphinx_book_theme==1.0.1',
        'sphinxcontrib_trio==1.1.2'
    ],
    'test': [
        'pytest',
        'pytest-cov'
    ]
}

packages = [
    'weatherly',
    'weatherly.api',
]

setup(
    name='weatherly',
    author='konradsic',
    url='https://github.com/konradsic/weatherly',
    project_urls={
        'Issues': 'https://github.com/konradsic/weatherly/issues',
    },
    version=version,
    packages=packages,
    license='MIT',
    description='A simple Python wrapper around WeatherAPI. Get current weather, forecast, history and more...',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.10.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Typing :: Typed',
    ],
)