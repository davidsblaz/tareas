import math

class ExperimentoFisico:
    pass

class CaidaLibre(ExperimentoFisico):
    def _init_(self, altura, gravedad):
        if altura < 0:
            print("Error: Altura no puede ser negativa")
            exit()
        if gravedad == 0:
            print("Error: Gravedad no puede ser cero")
            exit()
        self.altura = altura
        self.gravedad = gravedad

    def calcular_tiempo(self):
        tiempo = math.sqrt(2 * self.altura / self.gravedad)
        return tiempo

if __name__ == "_main_":
    experimento = CaidaLibre(10, 9.81)
    tiempo = experimento.calcular_tiempo()
    print(f"Tiempo de caída: {tiempo:.2f} segundos")