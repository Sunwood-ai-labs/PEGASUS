from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='pegasus-surf',
    version='0.1.1',
    description='A package for scraping websites and converting them to Markdown',
    author='Maki',
    author_email='sunwood.ai.labs@gmail.com',
    url='https://github.com/Sunwood-ai-labs/PEGASUS',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'requests',
        'markdownify',
        'beautifulsoup4',
        'loguru',
        'art',
    ],
    entry_points={
        'console_scripts': [
            'pegasus=pegasus.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)