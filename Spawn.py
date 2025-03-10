import random
import time

# Roleta para decidir se um monstro vai aparecer (50% de chance de "Sim")
aparece = random.choices(["Sim", "Não"], weights=[50, 50], k=1)[0]

if aparece == "Não":
    tempo_spawn = 3
    time.sleep(tempo_spawn)
    print("Nada apareceu dessa vez...")
else:
    # Regiões, locais e chances de spawn para cada horário
    regioes = {
        "1": {  # Askelon
            "nome": "Askelon",
            "locais": {
                "1": {"nome": "Floresta Densa", "monstros": {
                    "Gambá": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Morcego Gigante": {"raridade": "Incomum", "Dia": 0, "Noite": 25, "Madrugada": 25},
                    "Asa-Assasina": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Rato Gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Rei dos Ratos (Elite)": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                    "Bandido": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25}
                }},
                "2": {"nome": "Província", "monstros": {
                    "Gambá": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Lobo": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Bandido": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Rato Gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Rei dos Ratos (Elite)": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                }},
                "3": {"nome": "Caverna da Floresta Densa", "monstros": {
                    "Morcego Gigante": {"raridade": "Incomum", "Dia": 0, "Noite": 25, "Madrugada": 25},
                    "Aranha gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Aranha gigante (Elite)": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                    "Morcego gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Rato Gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Rei dos Ratos (Elite)": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                }}
            }
        },
        "2": {  # Netanya
            "nome": "Netanya",
            "locais": {
                "1": {"nome": "Floresta Temperada", "monstros": {
                    "Urso Pardo": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Urso Colossal": {"raridade": "Épico", "Dia": 4, "Noite": 4, "Madrugada": 4}
                }},
                "2": {"nome": "Área Sul", "monstros": {
                    "Esquilo": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Coelho": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Raposa": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Lobo": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Javalin Impetuoso": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Matilha de Gatos": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Gambá Peçonhento": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Falcão Críptico": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Zevantes": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                }},
                "3": {"nome": "Arredores do Cedro Ancestral", "monstros": {
                    "Esquilo": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Coelho": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Raposa Escarlate": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Espírito Verdejante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Zevantes": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                    "Avatar do Cedro Ancestral": {"raridade": "Épico", "Dia": 4, "Noite": 4, "Madrugada": 4}
                }},
                "4": {"nome": "Área Norte", "monstros": {
                    "Esquilo": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Coelho": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Raposa": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Javelin Alabarda": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Raposa Branca": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Gambá Friento": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                    "Zevantes": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                    "Harpia de Brumas Gélidas": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                    "Urso Colossal": {"raridade": "Épico", "Dia": 4, "Noite": 4, "Madrugada": 4}
                }}
            }
        }
    }

    def escolher_monstro(regiao, local, horario):
        """Escolhe um monstro baseado na região, local e horário."""
        if regiao not in regioes or local not in regioes[regiao]["locais"] or horario not in ["Dia", "Noite", "Madrugada"]:
            return None

        chances = regioes[regiao]["locais"][local]["monstros"]

        num = random.randint(1, 100)
        acumulado = 0

        for monstro, chance_por_horario in chances.items():
            acumulado += chance_por_horario[horario]  # Usa a chance específica do horário
            if num <= acumulado:
                return monstro

        return None

    # Escolha da região
    tempo_spawn = 3
    time.sleep(tempo_spawn)
    print("Escolha a região:")
    print("1 - Askelon")
    print("2 - Netanya")
    regiao = input("Digite 1: ")
    print('='*20)

    if regiao not in regioes:
        print("Região inválida. Reinicie o programa e tente novamente.")
        exit()

    nome_regiao = regioes[regiao]["nome"]

    # Escolha do local dentro da região
    print(f"Escolha o local dentro de {nome_regiao}:")
    for num, info in regioes[regiao]["locais"].items():
        print(f"{num} - {info['nome']}")
    local = input("Digite o número correspondente ao local: ")

    if local not in regioes[regiao]["locais"]:
        print("Local inválido. Reinicie o programa e tente novamente.")
        exit()


    nome_local = regioes[regiao]["locais"][local]["nome"]

    # Escolha do horário
    print('='*20)
    print("Escolha o horário:")
    print("1 - Dia")
    print("2 - Noite")
    print("3 - Madrugada")
    horario_opcao = input("Digite 1, 2 ou 3: ")
    print('='*20)

    horarios = {"1": "Dia", "2": "Noite", "3": "Madrugada"}
    horario = horarios.get(horario_opcao, None)

    if not horario:
        print("Horário inválido. Reinicie o programa e tente novamente.")
        exit()

    # Tempo de espera antes do spawn (entre 2 a 5 segundos)
    tempo_espera = 5
    print("Aguarde 5 segundos...")
    time.sleep(tempo_espera)

    monstro_apareceu = escolher_monstro(regiao, local, horario)

    if monstro_apareceu:
        print('='*30)
        print(f"Um \033[31m{monstro_apareceu}\033[0m apareceu na {nome_local} de {nome_regiao} durante a {horario}!")
        print('='*30)
    else:
        print('='*30)
        print("Nada apareceu dessa vez...")
        print('='*30)