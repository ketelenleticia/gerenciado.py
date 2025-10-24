def calcular_media(listaNotas):
    if not listaNotas:
        return 0
    return sum(listaNotas) / len(listaNotas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"