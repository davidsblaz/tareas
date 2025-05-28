# datos
 
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes",]
niveles_azucar = [130, 160, 95, 175, 160]     # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700]  # mg
presion_sistolica = [115, 130, 110, 125, 175]           # mmHg
presion_diastolica = [78, 79, 85,89 , 92]           # mmHg

# parametro de referencia 
azucar_min = 70
azucar_max = 140
sal_max = 2300

#funcion para calsificar presion arterial 
def clasificar_presion(sistolica, diastolica) :
    if sistolica >= 140 or diastolica >=90:
        return "hispertension etapa 2"
    elif 130 <= sistolica <=139 or 80 <= diastolica <= 89:
        return "hipertension etapa 1"
    elif 120 <= sistolica <= 129 and diastolica < 80:
        return "Elevada"
    elif sistolica < 120 and diastolica < 80:
        return "Normal"
    else:
        return "Indefinida"

# Evaluación diaria
print("Evaluación diaria:")
for i in range(len(dias)):
    alerta = []
    azucar = niveles_azucar[i]
    sal = niveles_sal[i]
    sis = presion_sistolica[i]
    dias_ = presion_diastolica[i]
    presion_cat = clasificar_presion(sis, dias_)

    if azucar < azucar_min or azucar > azucar_max:
        alerta.append("Azúcar fuera de rango")
    if sal > sal_max:
        alerta.append("Sal excedida")
    if presion_cat != "Normal":
        alerta.append(f"Presión arterial: {presion_cat}")

    print(f"{dias[i]}:")
    print(f"  Azúcar: {azucar} mg/dL")
    print(f"  Sal: {sal} mg")
    print(f"  Presión: {sis}/{dias_} mmHg ({presion_cat})")
    print(f"  Alertas: {'; '.join(alerta) if alerta else 'Todo en rango'}\n")

 # Promedios semanales
prom_azucar = sum(niveles_azucar) / len(niveles_azucar)
prom_sal = sum(niveles_sal) / len(niveles_sal)
prom_sis = sum(presion_sistolica) / len(presion_sistolica)
prom_dias = sum(presion_diastolica) / len(presion_diastolica)
presion_prom_cat = clasificar_presion(prom_sis, prom_dias)

print("Resumen semanal:")
print(f"  Promedio azúcar: {prom_azucar:.1f} mg/dL {'lol ' if prom_azucar > azucar_max else ''}")
print(f"  Promedio sal: {prom_sal:.1f} mg {'lol' if prom_sal > azucar_min else ''}")
print(f"  Promedio presión: {prom_sis:.1f}/{prom_dias:.1f} mmHg ({presion_prom_cat})")