import tkinter as tk
from create_contact import add_contact
from read_contact import read_contact
from update_contact import update_contact
from delete_contact import delete_contact


class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Contactos")
        self.filename = "friendsContact.txt"

        self.contact_adder = add_contact(self.filename)
        self.contact_reader = read_contact(self.filename)
        self.contact_updater = update_contact(self.filename)
        self.contact_deleter = delete_contact(self.filename)

        self.name_label = tk.Label(root, text="Nombre:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.number_label = tk.Label(root, text="Número:")
        self.number_label.grid(row=1, column=0)
        self.number_entry = tk.Entry(root)
        self.number_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Agregar", command=self.add_contact)
        self.add_button.grid(row=2, column=0)

        self.read_button = tk.Button(root, text="Leer", command=self.read_contact)
        self.read_button.grid(row=2, column=1)

        self.update_button = tk.Button(root, text="Actualizar", command=self.update_contact)
        self.update_button.grid(row=2, column=2)

        self.delete_button = tk.Button(root, text="Eliminar", command=self.delete_contact)
        self.delete_button.grid(row=2, column=3)

        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_contacts)
        self.clear_button.grid(row=2, column=4)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=3, column=0, columnspan=5)
        
    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        message = self.contact_adder.add(name, number)
        self.output_text.insert(tk.END, message + "\n")

    def read_contact(self):
        self.output_text.delete(1.0, tk.END)
        contacts = self.contact_reader.read()
        for contact in contacts:
            self.output_text.insert(tk.END, contact + "\n")

    def update_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        message = self.contact_updater.update(name, number)
        self.output_text.insert(tk.END, message + "\n")

    def delete_contact(self):
        name = self.name_entry.get()
        message = self.contact_deleter.delete(name)
        self.output_text.insert(tk.END, message + "\n")
    
    def clear_contacts(self):
        self.name_entry.delete(0, tk.END)  # Borra el campo de nombre
        self.number_entry.delete(0, tk.END)  # Borra el campo de número
        self.output_text.delete(1.0, tk.END)  # Borra la salida de texto

        
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
