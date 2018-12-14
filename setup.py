# -*- coding: utf-8 -*-

import setuptools
from setuptools import setup, find_packages
from bradocs4py import __version__

setup(
	name = 'bradocs4py',
	packages = find_packages(exclude = ['contrib', 'docs', 'tests*']),
	include_package_data = False,
	version = __version__,
	description = 'biblioteca Python que visa fornecer componentes para trabalhar com tipos de dados específicos da realidade brasileira.',
	long_description = 'biblioteca Python que visa fornecer componentes para trabalhar com tipos de dados específicos da realidade brasileira.',
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
