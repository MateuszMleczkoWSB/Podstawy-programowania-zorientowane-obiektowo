from abc import ABC, abstractmethod
from datetime import date, timedelta


class LibraryItem(ABC):
    def __init__(self, item_id: str, title: str, author: str, year: int):
        self._item_id = item_id
        self._title = title
        self._author = author
        self._year = year
        self._is_available = True

    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @property
    def is_available(self):
        return self._is_available

    def borrow(self):
        if not self._is_available:
            raise ValueError(f"'{self._title}' jest już wypożyczona.")
        self._is_available = False

    def return_item(self):
        self._is_available = True

    @abstractmethod
    def item_type(self) -> str:
        pass

    @abstractmethod
    def info(self) -> str:
        pass

    def __str__(self):
        status = "dostępna" if self._is_available else "wypożyczona"
        return f"ID: {self._item_id:<4} {self.item_type():<12} {self.info()} | {status}"


class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str, year: int, isbn: str):
        super().__init__(item_id, title, author, year)
        self._isbn = isbn

    def item_type(self) -> str:
        return "Książka"

    def info(self) -> str:
        return f"{self._title} – {self._author} (ISBN: {self._isbn}, {self._year})"


class Magazine(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str, year: int, issue_number: int):
        super().__init__(item_id, title, author, year)
        self._issue_number = issue_number

    def item_type(self) -> str:
        return "Czasopismo"

    def info(self) -> str:
        return f"{self._title} nr {self._issue_number} ({self._year})"


class AudioBook(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str, year: int, duration_minutes: int):
        super().__init__(item_id, title, author, year)
        self._duration_minutes = duration_minutes

    def item_type(self) -> str:
        return "Audiobook"

    def info(self) -> str:
        return f"{self._title} – {self._author} ({self._duration_minutes} min, {self._year})"


class Member:
    def __init__(self, member_id: str, first_name: str, last_name: str, email: str):
        self._member_id = member_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._loans: list["Loan"] = []

    @property
    def member_id(self):
        return self._member_id

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def add_loan(self, loan: "Loan"):
        self._loans.append(loan)

    def active_loans(self) -> list:
        return [loan for loan in self._loans if not loan.is_returned]

    def loan_history(self) -> list:
        return list(self._loans)

    def __str__(self):
        return f"ID: {self._member_id:<4} {self.full_name:<25} {self._email}"


class Loan:
    LOAN_DAYS = 14

    def __init__(self, loan_id: str, member: Member, item: LibraryItem):
        self._loan_id = loan_id
        self._member = member
        self._item = item
        self._borrow_date = date.today()
        self._due_date = self._borrow_date + timedelta(days=self.LOAN_DAYS)
        self._return_date = None

    @property
    def loan_id(self):
        return self._loan_id

    @property
    def item(self):
        return self._item

    @property
    def is_returned(self):
        return self._return_date is not None

    def complete_return(self):
        self._return_date = date.today()
        self._item.return_item()

    def is_overdue(self) -> bool:
        if self.is_returned:
            return False
        return date.today() > self._due_date

    def __str__(self):
        status = f"zwrócono {self._return_date}" if self.is_returned else f"termin: {self._due_date}"
        overdue = " [PRZETERMINOWANE]" if self.is_overdue() else ""
        return f"ID: {self._loan_id:<4} {self._item.title:<35} {self._member.full_name} | {status}{overdue}"


class Library:
    def __init__(self, name: str):
        self._name = name
        self._items: dict[str, LibraryItem] = {}
        self._members: dict[str, Member] = {}
        self._loans: dict[str, Loan] = {}
        self._loan_counter = 1

    def add_item(self, item: LibraryItem):
        self._items[item.item_id] = item

    def register_member(self, member: Member):
        self._members[member.member_id] = member

    def get_member(self, member_id: str) -> Member | None:
        return self._members.get(member_id)

    def borrow_item(self, member_id: str, item_id: str) -> Loan:
        member = self._members.get(member_id)
        item = self._items.get(item_id)

        if not member:
            raise ValueError(f"Nie znaleziono użytkownika o ID: {member_id}")
        if not item:
            raise ValueError(f"Nie znaleziono pozycji o ID: {item_id}")

        item.borrow()

        loan_id = str(self._loan_counter)
        self._loan_counter += 1

        loan = Loan(loan_id, member, item)
        member.add_loan(loan)
        self._loans[loan_id] = loan
        return loan

    def return_item(self, loan_id: str) -> Loan:
        loan = self._loans.get(loan_id)
        if not loan:
            raise ValueError(f"Nie znaleziono wypożyczenia o ID: {loan_id}")
        if loan.is_returned:
            raise ValueError(f"Wypożyczenie {loan_id} zostało już zwrócone.")
        loan.complete_return()
        return loan

    def search_by_title(self, phrase: str) -> list[LibraryItem]:
        return [item for item in self._items.values() if phrase.lower() in item.title.lower()]

    def all_items(self) -> list[LibraryItem]:
        return list(self._items.values())

    def all_members(self) -> list[Member]:
        return list(self._members.values())

    def active_loans(self) -> list[Loan]:
        return [loan for loan in self._loans.values() if not loan.is_returned]


def seed_data(library: Library):
    library.add_item(Book("1", "Wiedźmin: Ostatnie życzenie", "Andrzej Sapkowski", 1993, "978-83-7504-008-5"))
    library.add_item(Book("2", "1984", "George Orwell", 1949, "978-83-7506-298-8"))
    library.add_item(Book("3", "Władca Pierścieni", "J.R.R. Tolkien", 1954, "978-83-7469-000-0"))
    library.add_item(Magazine("4", "National Geographic", "Redakcja NG", 2024, 3))
    library.add_item(Magazine("5", "Polityka", "Redakcja Polityki", 2024, 15))
    library.add_item(AudioBook("6", "Sapiens", "Yuval Noah Harari", 2011, 900))

    library.register_member(Member("1", "Anna", "Kowalska", "anna@example.com"))
    library.register_member(Member("2", "Piotr", "Nowak", "piotr@example.com"))
    library.register_member(Member("3", "Maria", "Wiśniewska", "maria@example.com"))


def print_separator():
    print("-" * 60)


def menu_catalog(library: Library):
    print_separator()
    print("KATALOG ZBIORÓW")
    print_separator()
    for item in library.all_items():
        print(item)


def menu_members(library: Library):
    print_separator()
    print("LISTA UŻYTKOWNIKÓW")
    print_separator()
    for member in library.all_members():
        active = len(member.active_loans())
        print(f"{member} | wypożyczenia: {active}")


def menu_active_loans(library: Library):
    print_separator()
    print("AKTYWNE WYPOŻYCZENIA")
    print_separator()
    loans = library.active_loans()
    if not loans:
        print("Brak aktywnych wypożyczeń.")
    for loan in loans:
        print(loan)


def menu_borrow(library: Library):
    print_separator()
    print("WYPOŻYCZ POZYCJĘ")
    print_separator()
    print("Użytkownicy:")
    for member in library.all_members():
        print(f"  {member}")
    print()
    print("Dostępne pozycje:")
    for item in library.all_items():
        if item.is_available:
            print(f"  {item}")
    print()
    member_id = input("Podaj ID użytkownika: ").strip()
    item_id = input("Podaj ID pozycji:     ").strip()
    try:
        loan = library.borrow_item(member_id, item_id)
        print(f"Wypożyczono pomyślnie: {loan}")
    except ValueError as e:
        print(f"Błąd: {e}")


def menu_return(library: Library):
    print_separator()
    print("ZWRÓĆ POZYCJĘ")
    print_separator()
    loans = library.active_loans()
    if not loans:
        print("Brak aktywnych wypożyczeń.")
        return
    print("Aktywne wypożyczenia:")
    for loan in loans:
        print(f"  {loan}")
    print()
    loan_id = input("Podaj ID wypożyczenia: ").strip()
    try:
        loan = library.return_item(loan_id)
        print(f"Zwrócono pomyślnie: {loan}")
    except ValueError as e:
        print(f"Błąd: {e}")


def menu_search(library: Library):
    print_separator()
    print("WYSZUKAJ PO TYTULE")
    print_separator()
    phrase = input("Wpisz frazę: ").strip()
    results = library.search_by_title(phrase)
    if not results:
        print("Nie znaleziono żadnych pozycji.")
    for item in results:
        print(item)


def menu_member_history(library: Library):
    print_separator()
    print("HISTORIA WYPOŻYCZEŃ UŻYTKOWNIKA")
    print_separator()
    for member in library.all_members():
        print(f"  {member}")
    print()
    member_id = input("Podaj ID użytkownika: ").strip()
    member = library.get_member(member_id)
    if not member:
        print(f"Nie znaleziono użytkownika o ID: {member_id}")
        return
    history = member.loan_history()
    if not history:
        print("Brak historii wypożyczeń.")
    for loan in history:
        print(loan)


def main():
    library = Library("Miejska Biblioteka Publiczna")
    seed_data(library)

    menu = {
        "1": ("Katalog zbiorów", menu_catalog),
        "2": ("Lista użytkowników", menu_members),
        "3": ("Aktywne wypożyczenia", menu_active_loans),
        "4": ("Wypożycz pozycję", menu_borrow),
        "5": ("Zwróć pozycję", menu_return),
        "6": ("Wyszukaj po tytule", menu_search),
        "7": ("Historia wypożyczeń użytkownika", menu_member_history),
        "0": ("Wyjście", None),
    }

    while True:
        print("\n" + "=" * 60)
        print(f"  {library._name}")
        print("=" * 60)
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        print("=" * 60)

        choice = input("Wybierz opcję: ").strip()

        if choice == "0":
            print("Do widzenia!")
            break
        elif choice in menu:
            _, action = menu[choice]
            action(library)
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()