# -*- coding: utf-8 -*-

import re

from itertools import chain, compress

class ValidadorAP(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado do Amapá, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_AP.html.
	"""

	def __hashDigit(self, insc):
		pesos = range(9, 1, -1)

		if int(insc[:8]) in range(3000001, 3017000):
			p = 5
			d = 0
		elif int(insc[:8]) in range(3017001, 3019022):
			p = 9
			d = 1
		else:
			p = 0
			d = 0

		val = 11 - (p + sum(int(digito) * peso for digito, peso in zip(insc, pesos))) % 11

		if val == 11: return d

		return val if val < 10 else 0

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		p = re.compile('\\b03\\d{7}\\b')

		if not p.match(x): return False

		v = ValidadorAP()

		return v.__hashDigit(x) == int(x[8])
