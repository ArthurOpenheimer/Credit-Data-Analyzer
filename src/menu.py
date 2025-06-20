def menu():
    print("\nInsira os dados do cliente para classificação do risco de crédito:")

    dados = {}

    dados['laufkont'] = int(input(
        "\nStatus da conta corrente (laufkont):\n"
        "1: Sem conta corrente\n"
        "2: Saldo negativo\n"
        "3: Saldo entre 0 e 200 DM\n"
        "4: Saldo >= 200 DM ou salário há pelo menos 1 ano\n"
        "Escolha [1-4]: "
    ))

    dados['laufzeit'] = int(input("\nDuração do crédito em meses (laufzeit): "))

    dados['moral'] = int(input(
        "\nHistórico de crédito (moral):\n"
        "0: Atraso em pagamentos passados\n"
        "1: Conta crítica / outros créditos em outros lugares\n"
        "2: Nenhum crédito ou todos pagos devidamente\n"
        "3: Créditos existentes pagos devidamente até agora\n"
        "4: Todos os créditos neste banco pagos devidamente\n"
        "Escolha [0-4]: "
    ))

    dados['verw'] = int(input(
        "\nFinalidade do crédito (verw):\n"
        "0: Outros\n"
        "1: Carro novo\n"
        "2: Carro usado\n"
        "3: Móveis/equipamentos\n"
        "4: Rádio/TV\n"
        "5: Eletrodomésticos\n"
        "6: Reformas\n"
        "7: Educação\n"
        "8: Férias\n"
        "9: Requalificação profissional\n"
        "10: Negócios\n"
        "Escolha [0-10]: "
    ))

    dados['hoehe'] = float(input("\nMontante solicitado (hoehe): "))

    dados['sparkont'] = int(input(
        "\nConta poupança (sparkont):\n"
        "1: Sem conta poupança\n"
        "2: Menos de 100 DM\n"
        "3: Entre 100 e 500 DM\n"
        "4: Entre 500 e 1000 DM\n"
        "5: Acima de 1000 DM\n"
        "Escolha [1-5]: "
    ))

    dados['beszeit'] = int(input(
        "\nDuração do emprego atual (beszeit):\n"
        "1: Desempregado\n"
        "2: Menos de 1 ano\n"
        "3: 1 a 4 anos\n"
        "4: 4 a 7 anos\n"
        "5: Mais de 7 anos\n"
        "Escolha [1-5]: "
    ))

    dados['rate'] = int(input(
        "\nTaxa de prestação como % da renda disponível (rate):\n"
        "1: >= 35%\n"
        "2: 25% a 35%\n"
        "3: 20% a 25%\n"
        "4: < 20%\n"
        "Escolha [1-4]: "
    ))

    dados['famges'] = int(input(
        "\nEstado pessoal e sexo (famges):\n"
        "1: Homem divorciado/separado\n"
        "2: Mulher não solteira ou homem solteiro\n"
        "3: Homem casado/viúvo\n"
        "4: Mulher solteira\n"
        "Escolha [1-4]: "
    ))

    dados['buerge'] = int(input(
        "\nOutros devedores (buerge):\n"
        "1: Nenhum\n"
        "2: Co-aplicante\n"
        "3: Fiador\n"
        "Escolha [1-3]: "
    ))

    dados['wohnzeit'] = int(input(
        "\nTempo de residência atual (wohnzeit):\n"
        "1: Menos de 1 ano\n"
        "2: 1 a 4 anos\n"
        "3: 4 a 7 anos\n"
        "4: Mais de 7 anos\n"
        "Escolha [1-4]: "
    ))

    dados['verm'] = int(input(
        "\nPropriedade (verm):\n"
        "1: Nenhuma / desconhecida\n"
        "2: Carro ou outros\n"
        "3: Poupança de construção / seguro de vida\n"
        "4: Imóvel\n"
        "Escolha [1-4]: "
    ))

    dados['alter'] = int(input("\nIdade (alter): "))

    dados['weitkred'] = int(input(
        "\nOutros planos de parcelamento (weitkred):\n"
        "1: Banco\n"
        "2: Lojas\n"
        "3: Nenhum\n"
        "Escolha [1-3]: "
    ))

    dados['wohn'] = int(input(
        "\nMoradia (wohn):\n"
        "1: Gratuita\n"
        "2: Aluguel\n"
        "3: Própria\n"
        "Escolha [1-3]: "
    ))

    dados['bishkred'] = int(input(
        "\nNúmero de créditos existentes (bishkred):\n"
        "1: 1\n"
        "2: 2-3\n"
        "3: 4-5\n"
        "4: 6 ou mais\n"
        "Escolha [1-4]: "
    ))

    dados['beruf'] = int(input(
        "\nTipo de emprego (beruf):\n"
        "1: Desempregado / não qualificado (não residente)\n"
        "2: Não qualificado (residente)\n"
        "3: Empregado qualificado / funcionário\n"
        "4: Gerente / autônomo / altamente qualificado\n"
        "Escolha [1-4]: "
    ))

    dados['pers'] = int(input(
        "\nNúmero de pessoas a cargo (pers):\n"
        "1: 3 ou mais\n"
        "2: Até 2\n"
        "Escolha [1-2]: "
    ))

    dados['telef'] = int(input(
        "\nTelefone (telef):\n"
        "1: Não possui\n"
        "2: Sim (em nome do cliente)\n"
        "Escolha [1-2]: "
    ))

    dados['gastarb'] = int(input(
        "\nTrabalhador estrangeiro (gastarb):\n"
        "1: Sim\n"
        "2: Não\n"
        "Escolha [1-2]: "
    ))

    return dados
