# BRADocs4Py

BRADocs4Py é uma biblioteca que visa fornecer componentes para trabalhar com tipos de dados específicos da realidade brasileira.

Esta biblioteca surgiu mediante a necessidade de se ter tipos específicos que possibilitem lidar com documentos de identificação próprios do Brasil, como é o caso do Cadastro de Pessoa Física (CPF) e do Cadastro Nacional de Pessoa Jurídica (CNPJ).

Além de conter classes que representam o modelo computacional dos principais documentos brasileiros, esta biblioteca também disponibiliza classes que permitem a validação e a geração de números válidos para estes documentos; sendo estas últimas disponibilizadas exclusivamente para fins de testes computacionais.

> This software is coded and documented in portuguese only as it is intended to be used to generate the necessary files for the brazilian government regarding to digital bookkeeping.

## Requisitos

  * python

## Como instalar

    $ pip install bradocs4py

## Objetivos do Projeto

A ideia inicial do projeto e unificar em uma única biblioteca módulos que permitam representar computacionalmente e validar documentos brasileiros - inicialmente CPF e CNPJ, além de permitir a geração de números válidos para estes documentos.

## Compatibilidade do Projeto

O projeto inicialmente suportará apenas Python 3.6.5+.

Outras linguagens de programação poderão ter versões especificas conforme minha disponibilidade de tempo.

## Status do Projeto

O projeto está em fase inicial de desenvolvimento.

| Módulo                     |  Situação       |
|:---------------------------|:---------------:|
| DocumentoIdentificacao     |Funcional        |
| CPF                        |Funcional        |
| ValidadorCpf               |Funcional        |
| GeradorCpf                 |Funcional        |
| Cnpj                       |Funcional        |
| ValidadorCnpj              |Funcional        |
| GeradorCnpj                |Funcional        |
| InscricaoEstadual          |Funcional        |
| ValidadorInscricaoEstadual |Funcional        |
| GeradorInscricaoEstadual   |Não implementado |
| InscricaoSuframa           |Funcional        |
| ValidadorSuframa           |Funcional        |
| GeradorSuframa             |Funcional        |

### DocumentoIdentificacao

Classe abstrata, não podendo ser instanciada diretamente, serve como base para todas as classes que representam um documento de identificação ou qualquer outro documento brasileiro que necessite de validação.

### CPF

Classe usada para representar em código Pyhton um _Cadastro de Pessoa Física_ (CPF); permitindo representá-lo textualmente, com a devida formatação e identificar a sua validade.

#### Utilização

    >>> cpf = CPF('52513127765')
    >>> cpf
    '525.131.277-65'

    >>> cpf.isValid
    True

    >>> cpf.rawValue
    52513127765

    >>> cpf = CPF('abcdefghijk')
    >>> cpf.isValid
    False

    >>> print(cpf)
    abcdefghijk

    >>> print(cpf.rawValue)
    abcdefghijk

> Independente do conteúdo passado ao se criar uma instância de CPF, **sempre** obter-se-á uma instância deste. Caberá consultar a propriedade __isValid__ de uma instância de CPF para verificar se esta é válida ou não.

> A representação textual de uma instância de CPF só será exibida caso esta instância contenha um número válido de CPF; ao contrário será exibida a _string_ utilizada para criá-la.

> Para obter a _string_ utilizada ao instanciar um CPF, basta acessar a propriedade **rawValue** da instância criada.

### ValidadorCpf

Classe responsável por validar uma instância de CPF ou uma _string_ contendo a representação numérica de um CPF.

#### Utilização

    >>> cpf = CPF('abcdefghijk')
    >>> ValidadorCpf.validar(cpf)
    False

    >>> ValidadorCpf.validar('123.456.789-00')
    False

    Foi criado um CPF válido, porém foi digitado um caractere de separação diferente dos caracteres esperados (.-/ ). Mesmo assim, o validador informa tratar-se de um CPF correto
    >>> cpf = CPF('508,697,212-40')
    >>> ValidadorCpf.validar(cpf)
    True

### GeradorCpf

Classe responsável por gerar aleatoriamente um CPF válido.

#### Utilização

    >>> cpf = GeradorCpf.gerar()
    >>> cpf.isValid
    True

### Cnpj

Classe usada para representar em código Pyhton um _Cadastro Nacional de Pessoa Jurídica_ (CNPJ); permitindo representá-lo textualmente, com a devida formatação e identificar a sua validade.

#### Utilização

	>>> cnpj = Cnpj('abcdefghijklmn')
	>>> cnpj.isValid
	False

	>>> cnpj = Cnpj('12345678901234')
	>>> cnpj.isValid
	False

	>>> cnpj = Cnpj('19.658.147/0001-0O')
	>>> cnpj.isValid
	False

	>>> cnpj = Cnpj('19.658.147/0001-00')
	>>> cnpj.isValid
	True

> Independente do conteúdo passado ao se criar uma instância de CNPJ, **sempre** obter-se-á uma instância deste. Caberá consultar a propriedade __isValid__ de uma instância de CNPJ para verificar se esta é válida ou não.

> A representação textual de uma instância de CNPJ só será exibida caso esta instância contenha um número válido de CNPJ; ao contrário será exibida a _string_ utilizada para criá-la.

> Para obter a _string_ utilizada ao instanciar um CNPJ, basta acessar a propriedade **rawValue** da instância criada.

### ValidadorCnpj

Classe responsável por validar uma instância de CNPJ ou uma _string_ contendo a representação numérica de um CNPJ.

#### Utilização

	>>> cnpj = Cnpj('abcdefghijklmn')
	>>> ValidadorCnpj.validar(cnpj)
	False

	>>> cnpj = Cnpj('19.658.147/0001-0O')
	>>>ValidadorCnpj.validar(cnpj)
	False

	>>> ValidadorCnpj.validar('12345678901234')
	False

	>>> cnpj = Cnpj('34  633 423,0001/60')
	>>> ValidadorCnpj.validar(cnpj)
	True

	>>> ValidadorCnpj.validar('05.692.744/0001-38')
	True

### GeradorCnpj

Classe responsável por gerar aleatoriamente um CNPJ válido.

#### Utilização

    >>> cnpj = GeradorCnpj.gerar()
    >>> cnpj.isValid
    True

### InscricaoSuframa

Representa o número de inscrição na Superintendência da Zona Franca de Manaus (SUFRAMA)

> A SUFRAMA mantém controle sobre as empresas com insentivo fiscal, identificando-as através do número de _Inscrição SUFRAMA_.

A composição deste indicador é: _SS.NNNN.LLD_, onde:

**SS** representa o __código do setor de atividade__ da empresa, conforme exemplo abaixo:

| Código  | Descrição                   |
| :----:  | :---------------------------|
| 01 e 02 | Cooperativa                 |
| 10 e 11 | Comércio                    |
| 20      | Indústria com projeto pleno |
| 60      | Serviços                    |

**NNNN** número sequencial

**LL** representa o código da licalidade da Unidade Administrativa da Suframa que habilitou a empresa, conforme exemplo abaixo:


| Código | Descrição   |
| :----: | :-----------|
|   01   | Manaus      |
|   10   | Boa Vista   |
|   30   | Porto Velho |

**D** dígito verificador

#### Validação

* Campo numérico com 9 posições (incluindo o dígito verificador).
* Pode iniciar por 0 (zero), mas não pode iniciar por 00.
* Dígito verificador calculado por [__módulo 11__](https://pt.wikipedia.org/wiki/D%C3%ADgito_verificador#Módulo_11 "Método de cálculo do dígito verificador usando Módulo 11"), pesos 2 a 9.

#### Utilização

    >>> x = InscricaoSuframa('01.1234.129')
    >>> x.rawValue
    '011234129'
    >>> print(x)
    01.1234.129
    >>> x.isValid
    False

    >>> x = InscricaoSuframa('101580100')
    >>> x.rawValue
    '101580100'
    >>> print(x)
    10.1580.100
    >>> x.isValid
    True

    >>> x = InscricaoSuframa('1015801OO')
    >>> x.rawValue
    '1015801OO'
    >>> print(x)
    1015801OO
    >>> x.isValid
    False

### ValidadorSuframa

Valida uma instância de InscricaoSuframa ou uma _string_ contendo a representação numérica de uma Inscrição Suframa.

#### Utilização

    # Validação de uma _string_ representando uma Inscrição Suframa:
    >>> ValidadorSuframa.validar('101580100')
    True

    # Validação de uma _string_ representando uma Inscrição Suframa inválida (contendo caracteres não numéricos):
    >>> ValidadorSuframa.validar('1015801OO')
    False

    # Validação de uma instância de InscriçãoSuframa:
    >>> x = InscricaoSuframa('01.1234.129')
    >>> ValidadorSuframa.validar(x)
    False

### GeradorSuframa

Gera aleatoriamente uma Inscrição Suframa válida

    >>> x = GeradorSuframa.gerar()
    >>> x.isValid
    True

> **IMPORTANTE**: O __GeradorSuframa__ tem por objetivo ajudar estudantes, programadores, analistas de sistemas e testadores de código a gerar Inscrições Suframa válidas visando auxiliar as rotinas de testes de softwares em desenvolvimento.

> A má utilização dos dados gerados pelo __GeradorSuframa__ é de **total responsabilidade do usuário** desta biblioteca.

> As inscrições são geradas de forma aleatória, respeitando as leis de formação estabelecidas pela SUFRAMA.

### InscricaoEstadual

Representa, em código Pyhton, uma _Inscrição Estadual_ (IE), ou o registro do contribuinte no cadastro do ICMS mantido pela Receita Estadual; permitindo representá-lo textualmente, com a devida formatação e identificar a sua validade.

#### Utilização

    >>> ie = InscricaoEstadual('613.855.219.926', 'SP')
    >>> ie.isValid
    True
    >>> ie.rawValue
    '613855219926'
    >>> ie.UF
    'SP'
    >>> print(ie)
    613.855.219.926

### ValidadorInscricaoEstadual

Valida a consistência de uma instância de InscricaoEstadual ou uma _string_ contendo a representação numérica de uma Inscrição Estadual para uma determinada Unidade da Federação, informada juntamente com a representação numérica da IE a qual se deseja validar.

> A validação da Inscrição Estadual para cada Unidade da Federação brasileira, leva em consideração o disposto no [__Convênio 57/59__](http://www.sintegra.gov.br/conv_5795.html "ConvênioICMS 57/59"), como também as orientações e especificidades contidas na página [Conferências de Inscrições Estaduais](http://www.sintegra.gov.br/insc_est.html "Conferência de Inscrições Estaduais") do SINTEGRA.

#### Utilização

    >>> ie = InscricaoEstadual('613.855.219.926', 'SP')
    >>> ValidadorInscricaoEstadual.validar(ie)
    True

    >>> ValidadorInscricaoEstadual.validarStr('207653461', 'RN')
    True
    >>> ValidadorInscricaoEstadual.validarStr('209564598', 'TO')
    False

> **NOTA**: Caso não se deseje utilizar o __ValidadorInscricaoEstadual__, pode-se utilizar o validador específico para uma determinada Unidade da Federação.
<p>Cada Unidade da Federação brasileira possui o seu próprio validador, definido por: **Validador**XX, onde _XX_ deve ser substituído pela sigla da Unidade da Federação desejada.</p>
<p>O Exemplo a seguir mostra como utilizar somente o validador específico para o Ceará, visando validar uma Inscrição Estadual deste Estado:</p>

    >>> from bradocs4py.validadoresie import ValidadorCE
    >>> ValidadorCE.validar('1234567')
    False
    >>> ValidadorCE.validar('50374156-6')
    True

> **IMPORTANTE**: Ao contrário de ValidadorInscricaoEstadual, os validadores específicos de cada UF validam somente uma cadeia de caracteres (_string_) contendo o número representativo da Inscrição Estadual a ser validada.
