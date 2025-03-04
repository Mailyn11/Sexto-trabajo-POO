class add_contact:
    def __init__(self, filename):
        self.filename = filename
    
    def add(self, name, number):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    existing_name, existing_number = line.strip().split("!")
                    if existing_name == name or existing_number == number:
                        return "El contacto ya existe."
            with open(self.filename, "a") as file:
                file.write(f"{name}!{number}\n")
            return "Contacto agregado correctamente."
        except FileNotFoundError:
            with open(self.filename, "w") as file:
                file.write(f"{name}!{number}\n")
            return "Archivo creado y contacto agregado."