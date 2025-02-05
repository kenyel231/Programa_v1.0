class personaje:

    def __init__(self, nombre, raza, paisnatal, profesion, fuerza, defensa, vida):
        self.nombre = nombre
        self.raza = raza
        self.paisnatal = paisnatal
        self.profesion = profesion
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Raza: {self.raza}')
        print(f'Pais Natal: {self.paisnatal}')
        print(f'Profesión: {self.profesion}')
        print(f'Fuerza: {self.fuerza}')
        print(f'Defensa: {self.defensa}')
        print(f'Vida: {self.vida}')

    def subir_nivel(self, vida, fuerza, defensa):
        self.vida = self.vida + vida
        self.fuerza = self.fuerza + fuerza
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f'{self.nombre} ha muerto')

    def damage(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(f'{self.nombre} acaba de atacar al Yonko {enemigo.nombre} y le hace {damage} puntos de daño')
        if enemigo.esta_vivo():
            print(f'{enemigo.nombre} tiene {enemigo.vida} puntos de vida')
        else:
            enemigo.morir()

class Marine(personaje):
    def __init__(self, nombre, raza, paisnatal, profesion, fuerza, defensa, vida, rango):
        super().__init__(nombre, raza, paisnatal, profesion, fuerza, defensa, vida)
        self.rango = rango

mi_personaje = personaje('Zoro', 'Oni', 'Wano', 'Espadachin', 100, 100, 1000)
mi_enemigo = personaje('Kaido', 'Oni', 'Wano', 'Yonko', 10000, 1000, 10000)
el_marine = Marine('Smoker', 'Humano', 'North Blue', 'Vicealmirante', 100, 100, 1000, 'Vicealmirante')

# Obtener datos de jugador
nombreDeJugador = input("¿Cuál es tu nombre, aventurero?")
razaDeJugador = input("¿A qué tribu perteneces?")
paisNatalDeJugador = input("¿De qué lugar provienes?")