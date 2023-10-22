from setuptools import setup, find_packages

# Read README.md for the long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='postgres_to_sqlite',
    version='0.1.0',
    author='Your Name',
    author_email='youremail@example.com',
    description='A Python script for converting PostgreSQL dumps to SQLite.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/postgres_to_sqlite',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # Add any future dependencies here
    ],
    entry_points={
        'console_scripts': [
            'postgres_to_sqlite=postgres_to_sqlite:convert',
        ],
    },
)
