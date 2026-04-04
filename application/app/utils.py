from datetime import datetime

def dia_da_semana_atual():
    dias = ["SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA", "SABADO", "DOMINGO"]
    dia_num = datetime.now().weekday()  # retorna numero de 0 a 6
    return dias[dia_num]

def semestre_atual():
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    if mes_atual >= 1 and mes_atual <= 6:
        return str(ano_atual) + "1"
    else:
        return str(ano_atual) + "2"
    
def turno_atual():
    turnos = ["MATUTINO", "VESPERTINO", "NOTURNO"]
    hora_atual = datetime.now().hour
    if hora_atual >= 7 and hora_atual <= 12:
        return turnos[0]
    elif hora_atual > 12 and hora_atual < 18:
        return turnos[1]
    elif hora_atual >= 18 and hora_atual <= 22:
        return turnos[2]
    else:
        return "Turno inválido"

def hoje():
    return datetime.now().strftime("%d-%m-%Y")