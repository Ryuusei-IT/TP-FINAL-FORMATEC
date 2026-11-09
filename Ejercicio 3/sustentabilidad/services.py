def calcular_emisiones_carbono (carbono_kwh, factor_emision=0.4):
    """
    Calcula la emisión de carbono a partir del consumo en KWh.
    Eleva ValueError si el consumo es negativo
    """
    if carbono_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")
    return carbono_kwh * factor_emision


def obtener_metricas_consumo (registros):
    mayor_emision = 0.0
    total_global_emisiones = 0.0
    emisiones_por_planta = {}
    planta_mayor_consumo = ""

    for registro in registros:
        planta = registro.get("planta", "Planta Desconocida")
        consumo = registro.get("consumo_kwh", 0.0)

        emisiones = calcular_emisiones_carbono(consumo)
        total_global_emisiones += emisiones

        if planta not in emisiones_por_planta:
            emisiones_por_planta[planta] = 0.0

        emisiones_por_planta[planta] += emisiones

    for planta, emisiones in emisiones_por_planta.items():
        if emisiones > mayor_emision:
            mayor_emision = emisiones 
            planta_mayor_consumo = planta

    return {
        "total_global_emisiones": total_global_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "emisiones_por_planta": emisiones_por_planta
    }

# registro_historicos = [
#     {'planta':'Planta Norte', 'consumo_kwh':1200.0},
#     {'planta':'Planta Sur', 'consumo_kwh':2400.5},
#     {'planta':'Planta Este', 'consumo_kwh':1000.1},
#     {'planta':'Planta Oeste', 'consumo_kwh':1900.0},
#     {'planta':'Planta Norte', 'consumo_kwh':200.0},
# ]