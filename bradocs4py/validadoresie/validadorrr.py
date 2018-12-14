# -*- coding: utf-8 -*-

import re

class ValidadorRR(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado de Roraima, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_RR.html.
	"""

	def __hashDigit(self, insc):
		pesos = range(1, 9, 1)

		val = sum(int(digito) * peso for digito, peso in zip(insc, pesos)) % 9

		return val

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		p = re.compile('\\b24\\d{7}\\b')

		if len(x) != 9 or len(set(x)) == 1: return False

		v = ValidadorRR()

		return v.__hashDigit(x) == int(x[8])