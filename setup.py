from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in papers/__init__.py
from papers import __version__ as version

setup(
	name="papers",
	version=version,
	description="Custom App for Paper Industries",
	author="Finbyz Tech Pvt Ltd",
	author_email="info@finbyz.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
