# Aplikacja Desktopowa (pyQt5) do logowania treningow/progresji/kalorii/wagi/nastroju/regeneracji itd
# Zapisuje dane do bazy danych PostgreSql
# Funkcje:
# - dodawanie sesji treningowych i rzeczy tego typu (pierwsza linijka)
# - sledzenie wagi i kalorii z kazdego dnia + analiza podstawowa + wykres tygodniowy(jesli sie uda) (Pandas + Mathplotlib)
# - Zapisywanie notatek do kazdej sesjii
# - Eksport danych do CSV lub Excel (jesli sie uda)
# Funkcje rozbudowane:
# - integracja z API (FatSecret / OpenFoodFacts (do kalorii))
# - System PR
# - Tryb dziennika (Jak sie dzis czujesz?)
# - Prosty model regresyjny przewidujacy wzrost sily na podstawie danych
# - GUI z mozliwoscia zmiany motywu / dark mode

from Data.db_config import *

if __name__ == "__main__":
    if check_internet():
        INTERNET_CONNECTION = True
        print("Połączęnie z internetem nawiązane.")
        if connect_db():
            DATABASE_CONNECTION = True
            print("Połączono z bazą danych.")
        else:
            print("Brak połączęnia z bazą danych.")
    else:
        print("Brak połączenia z internetem.")
        
        
    if (INTERNET_CONNECTION and DATABASE_CONNECTION):
        createTables() 
    else:
        print("Nie utworzono tabeli.")