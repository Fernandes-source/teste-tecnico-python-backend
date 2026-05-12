registros = []

def acrescentar_registros(dado):
    registros.append(dado)

def mostrar_registros():
    return registros

def Diagnosticar():
    if not registros:
        return {"msg": "Não há registros de foco"}
    
    media = sum(r.nivel_foco for r in registros)/ len(registros)
    tempo_total = sum(r.tempo_minutos for r in registros)

    if media < 3:
        feedback = "Faça pausas maiores e não utilize o celular"
    elif media > 4:
        feedback = "Boa perfomance, continue"
    else:
        feedback = "equilibrado"

    return{
        "media_foco": media,
        "tempo_total": tempo_total,
        "feedback": feedback
    }