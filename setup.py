from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ins/__init__.py
from ins import __version__ as version

setup(
	name="ins",
	version=version,
	description="insmartsystems",
	author="Patel Asif Khan",
	author_email="aasif.p@indictranstech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
