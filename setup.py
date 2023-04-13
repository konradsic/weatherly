from setuptools import setup

version = "0.0.1"

readme = ""
with open("README.rst") as readme_file: 
    readme = readme_file.read()


requirements = []
with open("requirements.txt") as requirements_file: 
    requirements = requirements_file.read().splitlines()

extras_require = {
    "docs": [
        "sphinx==5.3.0"
    ]
}

packages = [

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
    description='A Python wrapper for the Discord API',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.10..0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        "Programming Language :: Python :: 3.11"
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)