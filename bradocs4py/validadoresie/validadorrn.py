# -*- coding: utf-8 -*-

import re

class ValidadorRN(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado do Rio Grande do Norte, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_RN.html.
	"""

	def __hashDigit(self, insc):
		pesos = range(len(insc), 1, -1)

		val = (10 * sum(int(digito) * peso for digito, peso in zip(insc, pesos))) % 11

		return val if val < 10 else 0

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		p = re.compile('\\b20\\d{7,8}\\b')

		if not p.match(x): return False

		v = ValidadorRN()

		return v.__hashDigit(x) == int(x[len(x) - 1])