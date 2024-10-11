class Pilas:
    def __init__(self):
        self.items = []
    def apilador(self, item):
        if len(self.items)<8:
            self.items.append(item)
            print(f"Se inserta {item}: {self.items} (tope = {len(self.items)})")
        else:
            print("La pila está llena. No se admiten más objetos.")
    def desapilador(self):
        if self.items:
            quitar = self.items.pop()
            print(f"Se va {quitar}: {self.items} (tope = {len(self.items)})")
        else:
            print("La pila esta vacia")

pila = Pilas()


pila.apilador('X')
pila.apilador('Y')
pila.desapilador()
pila.desapilador()
pila.desapilador()
pila.apilador('V')
pila.apilador('W')
pila.desapilador()
pila.apilador('R')