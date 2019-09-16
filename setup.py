from setuptools import setup, find_packages

setup(
    name="alan_pytridge",
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
)
