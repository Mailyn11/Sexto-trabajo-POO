class read_contact:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        try:
            with open(self.filename, "r") as file:
                contacts = file.readlines()
                if not contacts:
                    return ["No hay contactos guardados."]
                return [f"Nombre: {line.strip().split('!')[0]}, Número: {line.strip().split('!')[1]}" for line in contacts]
        except FileNotFoundError:
            return ["No hay contactos guardados."]