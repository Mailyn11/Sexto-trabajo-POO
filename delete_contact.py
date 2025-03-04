class delete_contact:
    def __init__(self, filename):
        self.filename = filename
    
    def delete(self, name):
        try:
            with open(self.filename, "r") as file:
                contacts = file.readlines()
            deleted = False
            with open(self.filename, "w") as file:
                for contact in contacts:
                    existing_name, _ = contact.strip().split("!")
                    if existing_name != name:
                        file.write(contact)
                    else:
                        deleted = True
            return "Contacto eliminado." if deleted else "El contacto no fue encontrado."
        except FileNotFoundError:
            return "No hay contactos guardados."