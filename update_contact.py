class update_contact:
    def __init__(self, filename):
        self.filename = filename
    
    def update(self, name, new_number):
        try:
            with open(self.filename, "r") as file:
                contacts = file.readlines()
            updated = False
            with open(self.filename, "w") as file:
                for contact in contacts:
                    existing_name, existing_number = contact.strip().split("!")
                    if existing_name == name:
                        file.write(f"{name}!{new_number}\n")
                        updated = True
                    else:
                        file.write(contact)
            return "Contacto actualizado." if updated else "El contacto no fue encontrado."
        except FileNotFoundError:
            return "No hay contactos guardados."