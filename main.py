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

class Institution:
    def __init__(self, name, location, employee):
        self.name = name
        self.location = location
        self.employee = employee
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

root = Tk()
root.geometry("1400x850")
root.title('proj_ppyt')

ramka_lista_obiektow = Frame(root)
ramka_lista_obiektow2 = Frame(root)
ramka_lista_obiektow3 = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_szczegoly_obiektu2 = Frame(root)
ramka_szczegoly_obiektu3 = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_lista_obiektow2.grid(row=0, column=1)
ramka_lista_obiektow3.grid(row=0, column=2)
# ramka_formularz.grid(row=0, column=2)
ramka_szczegoly_obiektu.grid(row=1, column=0)
ramka_szczegoly_obiektu2.grid(row=1, column=1)
ramka_szczegoly_obiektu3.grid(row=1, column=2)
ramka_mapa.grid(row=2, column=0, columnspan=3)

# ramka_lista_obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text='Lista Pracowników:')
label_lista_obiektow.grid(row=0, column=0)

listbox_lista_obiektow = Listbox(ramka_lista_obiektow, width=60, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=4)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text='Pokaz szczegóły')
button_pokaz_szczegoly.grid(row=2, column=0, sticky=W)

button_usun_obiekt = Button(ramka_lista_obiektow, text='Usuń')
button_usun_obiekt.grid(row=2, column=1)

button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj')
button_edytuj_obiekt.grid(row=2, column=2)

button_dodaj_obiekt = Button(ramka_lista_obiektow, text='Dodaj')
button_dodaj_obiekt.grid(row=2, column=3, sticky=E)

# ramka_lista_obiektow2
label_lista_obiektow2 = Label(ramka_lista_obiektow2, text='Lista Placówek:')
label_lista_obiektow2.grid(row=0, column=0)

listbox_lista_obiektow2 = Listbox(ramka_lista_obiektow2, width=60, height=10)
listbox_lista_obiektow2.grid(row=1, column=0, columnspan=4)

button_pokaz_szczegoly2 = Button(ramka_lista_obiektow2, text='Pokaz szczegóły')
button_pokaz_szczegoly2.grid(row=2, column=0, sticky=W)

button_usun_obiekt2 = Button(ramka_lista_obiektow2, text='Usuń')
button_usun_obiekt2.grid(row=2, column=1)

button_edytuj_obiekt2 = Button(ramka_lista_obiektow2, text='Edytuj')
button_edytuj_obiekt2.grid(row=2, column=2)

button_dodaj_obiekt2 = Button(ramka_lista_obiektow2, text='Dodaj')
button_dodaj_obiekt2.grid(row=2, column=3, sticky=E)

# ramka_lista_obiektow3
label_lista_obiektow3 = Label(ramka_lista_obiektow3, text='Lista Klientów:')
label_lista_obiektow3.grid(row=0, column=0)

listbox_lista_obiektow3 = Listbox(ramka_lista_obiektow3, width=60, height=10)
listbox_lista_obiektow3.grid(row=1, column=0, columnspan=4)

button_pokaz_szczegoly3 = Button(ramka_lista_obiektow3, text='Pokaz szczegóły')
button_pokaz_szczegoly3.grid(row=2, column=0, sticky=W)

button_usun_obiekt3 = Button(ramka_lista_obiektow3, text='Usuń')
button_usun_obiekt3.grid(row=2, column=1)

button_edytuj_obiekt3 = Button(ramka_lista_obiektow3, text='Edytuj')
button_edytuj_obiekt3.grid(row=2, column=2)

button_dodaj_obiekt3 = Button(ramka_lista_obiektow3, text='Dodaj')
button_dodaj_obiekt3.grid(row=2, column=3, sticky=E)

# ramka_formularz

# label_formularz = Label(ramka_formularz, text='Formularz:')
# label_formularz.grid(row=0, column=0)
#
# label_imie = Label(ramka_formularz, text='Imie:')
# label_imie.grid(row=1, column=0, sticky=W)
#
# label_nazwisko = Label(ramka_formularz, text='Nazwisko:')
# label_nazwisko.grid(row=2, column=0, sticky=W)
#
# label_miejscowosc = Label(ramka_formularz, text='Miejscowość:')
# label_miejscowosc.grid(row=3, column=0, sticky=W)
#
# label_post = Label(ramka_formularz, text='Post:')
# label_post.grid(row=4, column=0, sticky=W)
#
# entry_imie = Entry(ramka_formularz)
# entry_imie.grid(row=1, column=1)
#
# entry_nazwisko = Entry(ramka_formularz)
# entry_nazwisko.grid(row=2, column=1)
#
# entry_miejscowosc = Entry(ramka_formularz)
# entry_miejscowosc.grid(row=3, column=1)
#
# entry_post = Entry(ramka_formularz)
# entry_post.grid(row=4, column=1)
#
# button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj')
# button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

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