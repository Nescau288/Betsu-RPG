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
                "1": {"nome": "Floresta", "monstros": {
                    "Urso pardo de Netanya": {"Dia": 40, "Noite": 40, "Madrugada": 40},
                    "Urso Colocassal de Netanya (Elite)": {"Dia": 10, "Noite": 10, "Madrugada": 10},
                    "Aranha gigante": {"Dia": 0, "Noite": 80, "Madrugada": 80},
                    "Aranha gigante (Elite)": {"Dia": 0, "Noite": 10, "Madrugada": 10},
                    "Lobo da província": {"Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Rato gigante": {"Dia": 50, "Noite": 50, "Madrugada": 50},
                    "Rei dos Ratos (Elite)": {"Dia": 10, "Noite": 10, "Madrugada": 40},
                    "Asa-assasina": {"Dia": 40, "Noite": 40, "Madrugada": 10},
                    "Bandido": {"Dia": 40, "Noite": 40, "Madrugada": 40},
                    "Gambá": {"Dia": 50, "Noite": 50, "Madrugada": 50},
                    "Morcego gigante": {"Dia": 0, "Noite": 50, "Madrugada": 50}

                }},
                "2": {"nome": "Província", "monstros": {
                    "Lobo da província": {"Dia": 60, "Noite": 60, "Madrugada": 60},
                    "Bandido": {"Dia": 40, "Noite": 40, "Madrugada": 40}
                }},
                "3": {"nome": "Caverna", "monstros": {
                    "Aranha gigante": {"Dia": 0, "Noite": 80, "Madrugada": 80},
                    "Aranha gigante (Elite)": {"Dia": 0, "Noite": 10, "Madrugada": 10},
                    "Morcego gigante": {"Dia": 0, "Noite": 50, "Madrugada": 50}
                }}
            }
        },
        "2": {  # Netanya
            "nome": "Netanya",
            "locais": {
                "1": {"nome": "Montanha", "monstros": {
                    "Urso": {"Dia": 20, "Noite": 40, "Madrugada": 50},
                    "Lobo": {"Dia": 30, "Noite": 50, "Madrugada": 60},
                    "Orc": {"Dia": 35, "Noite": 45, "Madrugada": 50},
                    "Dragão": {"Dia": 15, "Noite": 25, "Madrugada": 30}
                }},
                "2": {"nome": "Vale Sombrio", "monstros": {
                    "Espectro": {"Dia": 10, "Noite": 40, "Madrugada": 60},
                    "Goblin": {"Dia": 30, "Noite": 40, "Madrugada": 50},
                    "Orc": {"Dia": 30, "Noite": 35, "Madrugada": 40},
                    "Dragão": {"Dia": 15, "Noite": 25, "Madrugada": 35}
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
    # print("2 - Netanya")
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
        print(f"Um {monstro_apareceu} apareceu na {nome_local} de {nome_regiao} durante a {horario}!")
        print('='*30)
    else:
        print('='*30)
        print("Nada apareceu dessa vez...")
        print('='*30)