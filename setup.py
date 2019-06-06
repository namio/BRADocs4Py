# -*- coding: utf-8 -*-

import setuptools
from setuptools import setup, find_packages
from bradocs4py import __version__

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name = 'bradocs4py',
	packages = find_packages(exclude = ['contrib', 'docs', 'tests*']),
	include_package_data = False,
	version = __version__,
	description = 'Corrige falha que invalidava chaves de acessos de notas fiscais eletrônicas emitidas com datas (ano e mês) anteriores à data corrente.',
	long_description = long_description,
	long_description_content_type="text/markdown",
	python_requires='>=3',
	author = 'Nâmio Evangelista Cavalcante de Sousa',
	author_email = 'namio.sousa@gmail.com',
	url = 'https://github.com/namio/BRADocs4Py.git',
	license = 'MIT',
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Natural Language :: Portuguese',
		'Natural Language :: Portuguese (Brazilian)',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	],
	keywords = 'cpf cnpj documentos brasileiros receita federal',
	zip_safe = True,
	)
