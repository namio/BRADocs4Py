# -*- coding: utf-8 -*-

import re

class ValidadorBA(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado da Bahia, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_BA.html.
	"""

	def __swap(self, arg, i, j):
		arg = list(arg)
		arg[i], arg[j] = arg[j], arg[i]

		return ''.join(arg)

	def __hashDigit(self, arg, posicao):
		modulo = 11 if int(arg[0]) in [6, 7, 9] else 10

		val = sum(int(digito) * peso for digito, peso in zip(arg, range(posicao, 1, -1))) % modulo

		return 0 if val < 2 else modulo - val

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		if (len(x) != 8 and len(x) != 9) or len(set(x)) == 1: return False

		v = ValidadorBA()

		x = v.__swap(x, len(x) - 2, len(x) - 1)

		return all(v.__hashDigit(x, i + len(x) - 1) == int(digito) for i, digito in enumerate(x[len(x)-2:]))

