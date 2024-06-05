def calcular_distancia(distancia_mapa_cm, escala):
    distancia_km = distancia_mapa_cm * escala / 100000  # Convertendo a escala para quilômetros
    return distancia_km

def main():
    # Dados fornecidos
    distancia_mapa_cm = 70
    escala = 250000

    # Calcula a distância em quilômetros
    distancia_km = calcular_distancia(distancia_mapa_cm, escala)

    print(f"A distância entre as cidades A e B é de aproximadamente {distancia_km:.2f} km.")

if __name__ == "__main__":
    main()
