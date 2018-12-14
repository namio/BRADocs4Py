# -*- coding: utf-8 -*-

import re

class ValidadorGO(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado de Goiás, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_GO.html.
	"""

	def __hashDigit(self, insc):
		pesos = range(9, 1, -1)

		val = sum(int(digito) * peso for digito, peso in zip(insc, pesos)) % 11

		if val > 1:
			return 11 - val

		if val == 1:
			return 1 if int(insc[:8]) in range(10103105, 10119998) else 0

		if val == 0: return 0

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		if x == '110944020' or x == '110944021': return True

		p = re.compile('\\b(10|11|15)\\d{7}\\b')

		if not p.match(x): return False

		if len(x) != 9 or len(set(x)) == 1: return False

		v = ValidadorGO()

		return v.__hashDigit(x) == int(x[8])
