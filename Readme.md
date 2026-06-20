# Biblioteka – projekt OOP w Pythonie

## Opis tematu

System zarządzania biblioteką umożliwia katalogowanie zbiorów (książki, czasopisma, audiobooki),
rejestrowanie członków oraz obsługę wypożyczeń i zwrotów z poziomu menu konsolowego.

---

## Klasy

**LibraryItem** (abstrakcyjna) – bazowy typ każdej pozycji bibliotecznej
Właściwości: `_item_id`, `_title`, `_author`, `_year`, `_is_available`
Metody: `borrow()`, `return_item()`, `item_type()` *(abstrakcyjna)*, `info()` *(abstrakcyjna)*

**Book** – reprezentuje książkę
Właściwości: `_isbn`
Metody: `item_type()`, `info()`

**Magazine** – reprezentuje czasopismo
Właściwości: `_issue_number`
Metody: `item_type()`, `info()`

**AudioBook** – reprezentuje audiobook
Właściwości: `_duration_minutes`
Metody: `item_type()`, `info()`

**Member** – członek biblioteki
Właściwości: `_member_id`, `_first_name`, `_last_name`, `_email`, `_loans`
Metody: `add_loan()`, `active_loans()`, `loan_history()`

**Loan** – pojedyncze wypożyczenie
Właściwości: `_loan_id`, `_member`, `_item`, `_borrow_date`, `_due_date`, `_return_date`
Metody: `complete_return()`, `is_overdue()`

**Library** – zarządza całym systemem
Właściwości: `_items`, `_members`,

## Uruchomienie

Projekt korzysta wyłącznie z biblioteki standardowej Pythona (`abc`, `datetime`).

    python Ex3.py