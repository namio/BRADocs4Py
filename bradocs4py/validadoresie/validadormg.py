# -*- coding: utf-8 -*-

import re

from itertools import chain, compress

class ValidadorMG(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado das Minas Gerais, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_AC.html.
	"""

	def __hashDigit(self, insc, posicao):
		if posicao == 12:
			pesos = [int(p) for p in list('12'*int(posicao/2))]

			x = insc[:3] + '0' + insc[3:]

			val = sum(int(digito) for digito in list(''.join([str(int(digito) * peso) for digito, peso in zip(x, pesos)])))

			return ((val // 10) % 10 + 1) * 10 - val

		pesos = chain(range(posicao - 10, 1, -1), range(11, 1, -1))

		x = insc

		val = sum(int(digito) * peso for digito, peso in zip(x, pesos)) % 11

		return 0 if val < 2 else 11 - val

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		if len(x) != 13 or len(set(x)) == 1: return False

		v = ValidadorMG()

		return all(v.__hashDigit(x, i + 12) == int(d) for i, d in enumerate(x[11:]))

