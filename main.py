from tkinter import *
import tkintermapview

employees: list = []
institutions: list = []
clients: list = []

class Employee:
    def __init__(self, name, surname, location, institution):
        self.name = name
        self.surname = surname
        self.location = location
        self.instytution = institution
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f"{self.location} {self.name}", marker_color_outside="blue")

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]

class Institution:
    def __init__(self, name, location, employee):
        self.name = name
        self.location = location
        self.employee = employee
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f"{self.location} {self.name}", marker_color_outside="black")

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]

class Client:
    def __init__(self, name, surname, location, pet, institution):
        self.name = name
        self.surname = surname
        self.location = location
        self.pet = pet
        self.instytution = institution
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f"{self.location} {self.name}")

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]

def open_form_employees():
    def add_employee() -> None:
        name = entry_imie.get()
        surname = entry_nazwisko.get()
        location = entry_miejscowosc.get()
        institution = entry_instytucja.get()

        employee = Employee(name=name, surname=surname, location=location, institution=institution)

        employees.append(employee)

        print(employees)

        entry_imie.delete(0, END)
        entry_nazwisko.delete(0, END)
        entry_miejscowosc.delete(0, END)
        entry_instytucja.delete(0, END)

        entry_imie.focus()
        show_employee()
    root_employee = Tk()
    root_employee.geometry("300x200")
    root_employee.title('formularz pracownik')
    ramka_formularz = Frame(root_employee)
    ramka_formularz.grid(row=0, column=0)
    # ramka_formularz

    label_formularz = Label(ramka_formularz, text='Formularz:')
    label_formularz.grid(row=0, column=0)

    label_imie = Label(ramka_formularz, text='Imie:')
    label_imie.grid(row=1, column=0, sticky=W)

    label_nazwisko = Label(ramka_formularz, text='Nazwisko:')
    label_nazwisko.grid(row=2, column=0, sticky=W)

    label_miejscowosc = Label(ramka_formularz, text='Miejscowość:')
    label_miejscowosc.grid(row=3, column=0, sticky=W)

    label_institution = Label(ramka_formularz, text='Instytucja:')
    label_institution.grid(row=4, column=0, sticky=W)

    entry_imie = Entry(ramka_formularz)
    entry_imie.grid(row=1, column=1)

    entry_nazwisko = Entry(ramka_formularz)
    entry_nazwisko.grid(row=2, column=1)

    entry_miejscowosc = Entry(ramka_formularz)
    entry_miejscowosc.grid(row=3, column=1)

    entry_instytucja = Entry(ramka_formularz)
    entry_instytucja.grid(row=4, column=1)

    button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj', command=add_employee)
    button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

    root_employee.mainloop()

def show_employee():
    listbox_lista_obiektow.delete(0, END)
    for idx, employee in enumerate(employees):
        listbox_lista_obiektow.insert(idx, f'{idx + 1}. {employee.name} {employee.surname}')

def remove_employee():
    i = listbox_lista_obiektow.index(ACTIVE)
    employees[i].marker.delete()
    employees[i].marker.delete()
    employees.pop(i)
    show_employee()

def open_edit_employees():

    i = listbox_lista_obiektow.index(ACTIVE)

    def update_employee(i):
        name = entry_imie.get()
        surname = entry_nazwisko.get()
        location = entry_miejscowosc.get()
        institution = entry_instytucja.get()

        employees[i].name = name
        employees[i].surname = surname
        employees[i].location = location
        employees[i].institution = institution

        employees[i].coordinates = employees[i].get_coordinates()
        employees[i].marker.delete()

        employees.pop(i)
        name = entry_imie.get()
        surname = entry_nazwisko.get()
        location = entry_miejscowosc.get()
        institution = entry_instytucja.get()

        employee = Employee(name=name, surname=surname, location=location, institution=institution)

        employees.append(employee)

        print(employees)

        entry_imie.delete(0, END)
        entry_nazwisko.delete(0, END)
        entry_miejscowosc.delete(0, END)
        entry_instytucja.delete(0, END)

        entry_imie.focus()
        show_employee()
        root_employee.destroy()

    root_employee = Tk()
    root_employee.geometry("300x200")
    root_employee.title('formularz pracownik')
    ramka_formularz = Frame(root_employee)
    ramka_formularz.grid(row=0, column=0)
    # ramka_formularz

    label_formularz = Label(ramka_formularz, text='Formularz:')
    label_formularz.grid(row=0, column=0)

    label_imie = Label(ramka_formularz, text='Imie:')
    label_imie.grid(row=1, column=0, sticky=W)

    label_nazwisko = Label(ramka_formularz, text='Nazwisko:')
    label_nazwisko.grid(row=2, column=0, sticky=W)

    label_miejscowosc = Label(ramka_formularz, text='Miejscowość:')
    label_miejscowosc.grid(row=3, column=0, sticky=W)

    label_institution = Label(ramka_formularz, text='Instytucja:')
    label_institution.grid(row=4, column=0, sticky=W)

    entry_imie = Entry(ramka_formularz)
    entry_imie.grid(row=1, column=1)

    entry_nazwisko = Entry(ramka_formularz)
    entry_nazwisko.grid(row=2, column=1)

    entry_miejscowosc = Entry(ramka_formularz)
    entry_miejscowosc.grid(row=3, column=1)

    entry_instytucja = Entry(ramka_formularz)
    entry_instytucja.grid(row=4, column=1)

    entry_imie.insert(0, employees[i].name)
    entry_nazwisko.insert(0, employees[i].surname)
    entry_miejscowosc.insert(0, employees[i].location)
    entry_instytucja.insert(0, employees[i].instytution)

    button_dodaj_obiekt = Button(ramka_formularz, text='Zapisz', command=lambda: update_employee(i))
    button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

    root_employee.mainloop()

def show_employee_details():
    i = listbox_lista_obiektow.index(ACTIVE)
    label_szczegoly_obiektu_name_wartosc.config(text=employees[i].name)
    label_szczegoly_obiektu_surname_wartosc.config(text=employees[i].surname)
    label_szczegoly_obiektu_miejscowosc_wartosc.config(text=employees[i].location)
    label_szczegoly_obiektu_institution_wartosc.config(text=employees[i].instytution)
    map_widget.set_zoom(15)
    map_widget.set_position(employees[i].coordinates[0], employees[i].coordinates[1])

def open_map_employee():
    i = listbox_lista_obiektow2.index(ACTIVE)

    root_map_employee = Toplevel()

    root_map_employee.geometry("1400x700")
    root_map_employee.title('mapa pracownicy')

    ramka_mapa1 = Frame(root_map_employee)
    ramka_mapa1.grid(row=0, column=0)

    map_widget1 = tkintermapview.TkinterMapView(ramka_mapa1, width=1400, height=700, corner_radius=0)
    map_widget1.grid(row=0, column=0, columnspan=2)
    map_widget1.set_position(52.23, 21.00)
    map_widget1.set_zoom(6)

    map_widget1.set_marker(institutions[i].coordinates[0], institutions[i].coordinates[1],
                                                   text=f"{institutions[i].location} {institutions[i].name}", marker_color_outside="black")

    for idx, employee in enumerate(employees):
        if employees[idx].instytution == institutions[i].name:
            map_widget1.set_marker(employees[idx].coordinates[0], employees[idx].coordinates[1],
                                                     text=f"{employees[idx].location} {employees[idx].name}", marker_color_outside="blue")

    root_map_employee.mainloop()

def open_form_institutions():
    def add_institution() -> None:
        name = entry_nazwa.get()
        location = entry_miejscowosc.get()
        employee = entry_pracownik.get()

        institution = Institution(name=name, location=location, employee=employee)

        institutions.append(institution)

        print(institutions)

        entry_nazwa.delete(0, END)
        entry_miejscowosc.delete(0, END)
        entry_pracownik.delete(0, END)
        entry_nazwa.focus()

        show_institution()

    root_institution = Tk()
    root_institution.geometry("300x200")
    root_institution.title('formularz instytucja')
    ramka_formularz = Frame(root_institution)
    ramka_formularz.grid(row=0, column=0)
    # ramka_formularz

    label_formularz = Label(ramka_formularz, text='Formularz:')
    label_formularz.grid(row=0, column=0)

    label_nazwa = Label(ramka_formularz, text='Nazwa:')
    label_nazwa.grid(row=1, column=0, sticky=W)

    label_miejscowosc = Label(ramka_formularz, text='Miejscowość:')
    label_miejscowosc.grid(row=2, column=0, sticky=W)

    label_pracownik = Label(ramka_formularz, text='Liczba pracowników:')
    label_pracownik.grid(row=3, column=0, sticky=W)

    entry_nazwa = Entry(ramka_formularz)
    entry_nazwa.grid(row=1, column=1)

    entry_miejscowosc = Entry(ramka_formularz)
    entry_miejscowosc.grid(row=2, column=1)

    entry_pracownik = Entry(ramka_formularz)
    entry_pracownik.grid(row=3, column=1)

    button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj', command=add_institution)
    button_dodaj_obiekt.grid(row=4, column=0, columnspan=2)

    root_institution.mainloop()

def show_institution():
    listbox_lista_obiektow2.delete(0, END)
    for idx, institution in enumerate(institutions):
        listbox_lista_obiektow2.insert(idx, f'{idx + 1}. {institution.name} {institution.location}')

def remove_institution():
    i = listbox_lista_obiektow2.index(ACTIVE)
    institutions[i].marker.delete()
    institutions.pop(i)
    show_institution()

def open_edit_institution():

    i = listbox_lista_obiektow2.index(ACTIVE)

    def update_institution(i):
        name = entry_nazwa.get()
        location = entry_miejscowosc.get()
        employee = entry_pracownik.get()

        institutions[i].name = name
        institutions[i].location = location
        institutions[i].employee = employee

        institutions[i].coordinates = institutions[i].get_coordinates()
        institutions[i].marker.delete()

        institutions.pop(i)
        name = entry_nazwa.get()
        location = entry_miejscowosc.get()
        employee = entry_pracownik.get()

        institution = Institution(name=name, location=location, employee=employee)

        institutions.append(institution)

        print(institutions)

        entry_nazwa.delete(0, END)
        entry_miejscowosc.delete(0, END)
        entry_pracownik.delete(0, END)

        entry_nazwa.focus()
        show_institution()
        root_institution.destroy()

    root_institution = Tk()
    root_institution.geometry("300x200")
    root_institution.title('formularz instytucja')
    ramka_formularz = Frame(root_institution)
    ramka_formularz.grid(row=0, column=0)
    # ramka_formularz

    label_formularz = Label(ramka_formularz, text='Formularz:')
    label_formularz.grid(row=0, column=0)

    label_nazwa = Label(ramka_formularz, text='Nazwa:')
    label_nazwa.grid(row=1, column=0, sticky=W)

    label_miejscowosc = Label(ramka_formularz, text='Miejscowość:')
    label_miejscowosc.grid(row=2, column=0, sticky=W)

    label_pracownik = Label(ramka_formularz, text='Liczba pracowników:')
    label_pracownik.grid(row=3, column=0, sticky=W)

    entry_nazwa = Entry(ramka_formularz)
    entry_nazwa.grid(row=1, column=1)

    entry_miejscowosc = Entry(ramka_formularz)
    entry_miejscowosc.grid(row=2, column=1)

    entry_pracownik = Entry(ramka_formularz)
    entry_pracownik.grid(row=3, column=1)

    entry_nazwa.insert(0, institutions[i].name)
    entry_miejscowosc.insert(0, institutions[i].location)
    entry_pracownik.insert(0, institutions[i].employee)

    button_dodaj_obiekt = Button(ramka_formularz, text='Zapisz', command=lambda: update_institution(i))
    button_dodaj_obiekt.grid(row=4, column=0, columnspan=2)

    root_institution.mainloop()

def show_institution_details():
    i = listbox_lista_obiektow2.index(ACTIVE)
    label_szczegoly_obiektu2_name_wartosc.config(text=institutions[i].name)
    label_szczegoly_obiektu_miejscowosc2_wartosc.config(text=institutions[i].location)
    label_szczegoly_obiektu_employees_wartosc.config(text=institutions[i].employee)
    map_widget.set_zoom(15)
    map_widget.set_position(institutions[i].coordinates[0], institutions[i].coordinates[1])

def open_form_clients():
    def add_client() -> None:
        name = entry_imie.get()
        surname = entry_nazwisko.get()
        location = entry_miejscowosc.get()
        institution = entry_instytucja.get()
        pet = entry_pupil.get()

        client = Client(name=name, surname=surname, location=location, institution=institution, pet=pet)

        clients.append(client)

        print(clients)

        entry_imie.delete(0, END)
        entry_nazwisko.delete(0, END)
        entry_miejscowosc.delete(0, END)
        entry_instytucja.delete(0, END)
        entry_pupil.delete(0, END)

        entry_imie.focus()
        show_client()
    root_client = Tk()
    root_client.geometry("300x200")
    root_client.title('formularz klient')
    ramka_formularz = Frame(root_client)
    ramka_formularz.grid(row=0, column=0)

    # ramka_formularz

    label_formularz = Label(ramka_formularz, text='Formularz:')
    label_formularz.grid(row=0, column=0)

    label_imie = Label(ramka_formularz, text='Imie:')
    label_imie.grid(row=1, column=0, sticky=W)

    label_nazwisko = Label(ramka_formularz, text='Nazwisko:')
    label_nazwisko.grid(row=2, column=0, sticky=W)

    label_miejscowosc = Label(ramka_formularz, text='Miejscowość:')
    label_miejscowosc.grid(row=3, column=0, sticky=W)

    label_institution = Label(ramka_formularz, text='Instytucja:')
    label_institution.grid(row=4, column=0, sticky=W)

    label_pet = Label(ramka_formularz, text='Pupil:')
    label_pet.grid(row=5, column=0, sticky=W)

    entry_imie = Entry(ramka_formularz)
    entry_imie.grid(row=1, column=1)

    entry_nazwisko = Entry(ramka_formularz)
    entry_nazwisko.grid(row=2, column=1)

    entry_miejscowosc = Entry(ramka_formularz)
    entry_miejscowosc.grid(row=3, column=1)

    entry_instytucja = Entry(ramka_formularz)
    entry_instytucja.grid(row=4, column=1)

    entry_pupil = Entry(ramka_formularz)
    entry_pupil.grid(row=5, column=1)

    button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj', command=add_client)
    button_dodaj_obiekt.grid(row=6, column=0, columnspan=2)

    root_client.mainloop()


def show_client():
    listbox_lista_obiektow3.delete(0, END)
    for idx, client in enumerate(clients):
        listbox_lista_obiektow3.insert(idx, f'{idx + 1}. {client.name} {client.surname}')

def remove_client():
    i = listbox_lista_obiektow3.index(ACTIVE)
    clients[i].marker.delete()
    clients.pop(i)
    show_client()

def open_edit_clients():

    i = listbox_lista_obiektow3.index(ACTIVE)

    def update_client(i):
        name = entry_imie.get()
        surname = entry_nazwisko.get()
        location = entry_miejscowosc.get()
        institution = entry_instytucja.get()
        pet = entry_pupil.get()

        clients[i].name = name
        clients[i].surname = surname
        clients[i].location = location
        clients[i].institution = institution
        clients[i].pet = pet

        clients[i].coordinates = clients[i].get_coordinates()
        clients[i].marker.delete()

        clients.pop(i)
        name = entry_imie.get()
        surname = entry_nazwisko.get()
        location = entry_miejscowosc.get()
        institution = entry_instytucja.get()
        pet = entry_pupil.get()

        client = Client(name=name, surname=surname, location=location, institution=institution, pet=pet)

        clients.append(client)

        print(clients)

        entry_imie.delete(0, END)
        entry_nazwisko.delete(0, END)
        entry_miejscowosc.delete(0, END)
        entry_instytucja.delete(0, END)
        entry_pupil.delete(0, END)

        entry_imie.focus()
        show_client()
        root_client.destroy()

    root_client = Tk()
    root_client.geometry("300x200")
    root_client.title('formularz klient')
    ramka_formularz = Frame(root_client)
    ramka_formularz.grid(row=0, column=0)
    # ramka_formularz

    label_formularz = Label(ramka_formularz, text='Formularz:')
    label_formularz.grid(row=0, column=0)

    label_imie = Label(ramka_formularz, text='Imie:')
    label_imie.grid(row=1, column=0, sticky=W)

    label_nazwisko = Label(ramka_formularz, text='Nazwisko:')
    label_nazwisko.grid(row=2, column=0, sticky=W)

    label_miejscowosc = Label(ramka_formularz, text='Miejscowość:')
    label_miejscowosc.grid(row=3, column=0, sticky=W)

    label_institution = Label(ramka_formularz, text='Instytucja:')
    label_institution.grid(row=4, column=0, sticky=W)

    label_pet = Label(ramka_formularz, text='Pupil:')
    label_pet.grid(row=5, column=0, sticky=W)

    entry_imie = Entry(ramka_formularz)
    entry_imie.grid(row=1, column=1)

    entry_nazwisko = Entry(ramka_formularz)
    entry_nazwisko.grid(row=2, column=1)

    entry_miejscowosc = Entry(ramka_formularz)
    entry_miejscowosc.grid(row=3, column=1)

    entry_instytucja = Entry(ramka_formularz)
    entry_instytucja.grid(row=4, column=1)

    entry_pupil = Entry(ramka_formularz)
    entry_pupil.grid(row=5, column=1)

    entry_imie.insert(0, clients[i].name)
    entry_nazwisko.insert(0, clients[i].surname)
    entry_miejscowosc.insert(0, clients[i].location)
    entry_instytucja.insert(0, clients[i].instytution)
    entry_pupil.insert(0, clients[i].pet)

    button_dodaj_obiekt = Button(ramka_formularz, text='Zapisz', command=lambda: update_client(i))
    button_dodaj_obiekt.grid(row=6, column=0, columnspan=2)

    root_client.mainloop()

def show_client_details():
    i = listbox_lista_obiektow3.index(ACTIVE)
    label_szczegoly_obiektu3_name_wartosc.config(text=clients[i].name)
    label_szczegoly_obiektu3_surname_wartosc.config(text=clients[i].surname)
    label_szczegoly_obiektu3_miejscowosc2_wartosc.config(text=clients[i].location)
    label_szczegoly_obiektu3_institution_wartosc.config(text=clients[i].instytution)
    label_szczegoly_obiektu_pet_wartosc.config(text=clients[i].pet)
    map_widget.set_zoom(15)
    map_widget.set_position(clients[i].coordinates[0], clients[i].coordinates[1])

def open_map_client():
    i = listbox_lista_obiektow2.index(ACTIVE)

    root_map_client = Toplevel()

    root_map_client.geometry("1400x700")
    root_map_client.title('mapa klienci')

    ramka_mapa2 = Frame(root_map_client)
    ramka_mapa2.grid(row=0, column=0)

    map_widget2 = tkintermapview.TkinterMapView(ramka_mapa2, width=1400, height=700, corner_radius=0)
    map_widget2.grid(row=0, column=0, columnspan=2)
    map_widget2.set_position(52.23, 21.00)
    map_widget2.set_zoom(6)

    map_widget2.set_marker(institutions[i].coordinates[0], institutions[i].coordinates[1],
                                                   text=f"{institutions[i].location} {institutions[i].name}", marker_color_outside="black")

    for idx, client in enumerate(clients):
        if clients[idx].instytution == institutions[i].name:
            map_widget2.set_marker(clients[idx].coordinates[0], clients[idx].coordinates[1],
                                                     text=f"{clients[idx].location} {clients[idx].name}")

    root_map_client.mainloop()

root = Tk()

root.geometry("1400x900")
root.title('proj_ppyt')

ramka_lista_obiektow = Frame(root)
ramka_lista_obiektow2 = Frame(root)
ramka_lista_obiektow3 = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_szczegoly_obiektu2 = Frame(root)
ramka_szczegoly_obiektu3 = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_lista_obiektow2.grid(row=0, column=1)
ramka_lista_obiektow3.grid(row=0, column=2)
ramka_szczegoly_obiektu.grid(row=1, column=0, pady=8)
ramka_szczegoly_obiektu2.grid(row=1, column=1, pady=8)
ramka_szczegoly_obiektu3.grid(row=1, column=2, pady=8)
ramka_mapa.grid(row=2, column=0, columnspan=3)

# ramka_lista_obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text='Lista Pracowników:')
label_lista_obiektow.grid(row=0, column=0, pady=8)

listbox_lista_obiektow = Listbox(ramka_lista_obiektow, width=60, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=4)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_employee_details)
button_pokaz_szczegoly.grid(row=2, column=0, sticky=W, pady=8)

button_usun_obiekt = Button(ramka_lista_obiektow, text='Usuń', command=remove_employee)
button_usun_obiekt.grid(row=2, column=1)

button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj', command=open_edit_employees)
button_edytuj_obiekt.grid(row=2, column=2)

button_dodaj_obiekt = Button(ramka_lista_obiektow, text='Dodaj', command=open_form_employees)
button_dodaj_obiekt.grid(row=2, column=3, sticky=E)

# ramka_lista_obiektow2
label_lista_obiektow2 = Label(ramka_lista_obiektow2, text='Lista Placówek:')
label_lista_obiektow2.grid(row=0, column=0, pady=8)

button_map1 = Button(ramka_lista_obiektow2, text='Wyświetl pracowników wybranej placówki', command=open_map_employee)
button_map1.grid(row=0, column=1, columnspan=3)

listbox_lista_obiektow2 = Listbox(ramka_lista_obiektow2, width=60, height=10)
listbox_lista_obiektow2.grid(row=1, column=0, columnspan=4)

button_pokaz_szczegoly2 = Button(ramka_lista_obiektow2, text='Pokaż szczegóły', command=show_institution_details)
button_pokaz_szczegoly2.grid(row=2, column=0, sticky=W, pady=8)

button_usun_obiekt2 = Button(ramka_lista_obiektow2, text='Usuń', command=remove_institution)
button_usun_obiekt2.grid(row=2, column=1)

button_edytuj_obiekt2 = Button(ramka_lista_obiektow2, text='Edytuj', command=open_edit_institution)
button_edytuj_obiekt2.grid(row=2, column=2)

button_dodaj_obiekt2 = Button(ramka_lista_obiektow2, text='Dodaj', command=open_form_institutions)
button_dodaj_obiekt2.grid(row=2, column=3, sticky=E)

# ramka_lista_obiektow3
label_lista_obiektow3 = Label(ramka_lista_obiektow3, text='Lista Klientów:')
label_lista_obiektow3.grid(row=0, column=0, pady=8)

button_map2 = Button(ramka_lista_obiektow3, text='Wyświetl klientów wybranej placówki', command=open_map_client)
button_map2.grid(row=0, column=1, columnspan=3)

listbox_lista_obiektow3 = Listbox(ramka_lista_obiektow3, width=60, height=10)
listbox_lista_obiektow3.grid(row=1, column=0, columnspan=4)

button_pokaz_szczegoly3 = Button(ramka_lista_obiektow3, text='Pokaż szczegóły', command=show_client_details)
button_pokaz_szczegoly3.grid(row=2, column=0, sticky=W, pady=8)

button_usun_obiekt3 = Button(ramka_lista_obiektow3, text='Usuń', command=remove_client)
button_usun_obiekt3.grid(row=2, column=1)

button_edytuj_obiekt3 = Button(ramka_lista_obiektow3, text='Edytuj', command=open_edit_clients)
button_edytuj_obiekt3.grid(row=2, column=2)

button_dodaj_obiekt3 = Button(ramka_lista_obiektow3, text='Dodaj', command=open_form_clients)
button_dodaj_obiekt3.grid(row=2, column=3, sticky=E)

# ramka_szczegoly_obiektow
label_pokaz_szczegoly = Label(ramka_szczegoly_obiektu, text='Szczegóły Pracownika:')
label_pokaz_szczegoly.grid(row=0, column=0)

label_szczegoly_obiektu_name = Label(ramka_szczegoly_obiektu, text='Imię:')
label_szczegoly_obiektu_name.grid(row=1, column=0)

label_szczegoly_obiektu_name_wartosc = Label(ramka_szczegoly_obiektu, text='....')
label_szczegoly_obiektu_name_wartosc.grid(row=1, column=1)

label_szczegoly_obiektu_surname = Label(ramka_szczegoly_obiektu, text='Nazwisko:')
label_szczegoly_obiektu_surname.grid(row=1, column=2)

label_szczegoly_obiektu_surname_wartosc = Label(ramka_szczegoly_obiektu, text='....')
label_szczegoly_obiektu_surname_wartosc.grid(row=1, column=3)

label_szczegoly_obiektu_miejscowosc = Label(ramka_szczegoly_obiektu, text='Miejscowość:')
label_szczegoly_obiektu_miejscowosc.grid(row=1, column=4)

label_szczegoly_obiektu_miejscowosc_wartosc = Label(ramka_szczegoly_obiektu, text='....')
label_szczegoly_obiektu_miejscowosc_wartosc.grid(row=1, column=5)

label_szczegoly_obiektu_institution = Label(ramka_szczegoly_obiektu, text='Placówka:')
label_szczegoly_obiektu_institution.grid(row=1, column=6)

label_szczegoly_obiektu_institution_wartosc = Label(ramka_szczegoly_obiektu, text='....')
label_szczegoly_obiektu_institution_wartosc.grid(row=1, column=7)

# ramka_szczegoly_obiektow2
label_pokaz_szczegoly2 = Label(ramka_szczegoly_obiektu2, text='Szczegóły Placówki:')
label_pokaz_szczegoly2.grid(row=0, column=0)

label_szczegoly_obiektu2_name = Label(ramka_szczegoly_obiektu2, text='Nazwa:')
label_szczegoly_obiektu2_name.grid(row=1, column=0)

label_szczegoly_obiektu2_name_wartosc = Label(ramka_szczegoly_obiektu2, text='....')
label_szczegoly_obiektu2_name_wartosc.grid(row=1, column=1)

label_szczegoly_obiektu_miejscowosc2 = Label(ramka_szczegoly_obiektu2, text='Miejscowość:')
label_szczegoly_obiektu_miejscowosc2.grid(row=1, column=2)

label_szczegoly_obiektu_miejscowosc2_wartosc = Label(ramka_szczegoly_obiektu2, text='....')
label_szczegoly_obiektu_miejscowosc2_wartosc.grid(row=1, column=3)

label_szczegoly_obiektu_employees = Label(ramka_szczegoly_obiektu2, text='Liczba pracowników:')
label_szczegoly_obiektu_employees.grid(row=1, column=4)

label_szczegoly_obiektu_employees_wartosc = Label(ramka_szczegoly_obiektu2, text='....')
label_szczegoly_obiektu_employees_wartosc.grid(row=1, column=5)

# ramka_szczegoly_obiektow3
label_pokaz_szczegoly3 = Label(ramka_szczegoly_obiektu3, text='Szczegóły Klienta:')
label_pokaz_szczegoly3.grid(row=0, column=0)

label_szczegoly_obiektu3_name = Label(ramka_szczegoly_obiektu3, text='Imie:')
label_szczegoly_obiektu3_name.grid(row=1, column=0)

label_szczegoly_obiektu3_name_wartosc = Label(ramka_szczegoly_obiektu3, text='....')
label_szczegoly_obiektu3_name_wartosc.grid(row=1, column=1)

label_szczegoly_obiektu3_surname = Label(ramka_szczegoly_obiektu3, text='Nazwisko:')
label_szczegoly_obiektu3_surname.grid(row=1, column=2)

label_szczegoly_obiektu3_surname_wartosc = Label(ramka_szczegoly_obiektu3, text='....')
label_szczegoly_obiektu3_surname_wartosc.grid(row=1, column=3)

label_szczegoly_obiektu3_miejscowosc2 = Label(ramka_szczegoly_obiektu3, text='Miejscowość:')
label_szczegoly_obiektu3_miejscowosc2.grid(row=1, column=4)

label_szczegoly_obiektu3_miejscowosc2_wartosc = Label(ramka_szczegoly_obiektu3, text='....')
label_szczegoly_obiektu3_miejscowosc2_wartosc.grid(row=1, column=5)

label_szczegoly_obiektu_pet = Label(ramka_szczegoly_obiektu3, text='Imie pupila:')
label_szczegoly_obiektu_pet.grid(row=1, column=6)

label_szczegoly_obiektu_pet_wartosc = Label(ramka_szczegoly_obiektu3, text='....')
label_szczegoly_obiektu_pet_wartosc.grid(row=1, column=7)

label_szczegoly_obiektu3_institution = Label(ramka_szczegoly_obiektu3, text='Placówka:')
label_szczegoly_obiektu3_institution.grid(row=1, column=8)

label_szczegoly_obiektu3_institution_wartosc = Label(ramka_szczegoly_obiektu3, text='....')
label_szczegoly_obiektu3_institution_wartosc.grid(row=1, column=9)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1400, height=600, corner_radius=0)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)

root.mainloop()