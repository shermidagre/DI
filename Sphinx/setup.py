from distutils.core import setup
from setuptools.config.expand import find_packages

setup(
    name='ejemplo distro', version='1.0',
    description='Ejemplo de distro', author='Samuel Hermida Gregores',
    author_email='shermdiagre@gmail.com', scripts=["main.py"],
    py_modules=['ejemplo_distro'], packages = find_packages(), #["fontes","documentacion"],
    package_data = {
        "documentacion": ["html/*.html", "html/searchindex.js","html/_static/*.js","html/_static/*.css"]
    }
)

