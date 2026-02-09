# Survey Analysis

Projekt do analizy danych z ankiet w Pythonie. Wczytuje dane z pliku CSV, czyści je, wykonuje analizę statystyczną i umożliwia wyświetlenie wykresów.

## Wymagania

- Python 3.x
- pandas
- numpy
- matplotlib

Instalacja zależności:

```bash
pip install pandas numpy matplotlib
```

## Struktura projektu

```
survey_analysis/
├── main.py              # Punkt wejścia, uruchamia pipeline i analizę
├── data/
│   └── survey_results.csv   # Dane ankiet (wejście/wyjście)
├── scripts/
│   ├── data_cleaning.py # Czyszczenie i normalizacja danych
│   ├── analysis.py      # Analiza statystyczna (wiek, satysfakcja, korelacje)
│   └── plots.py         # Generowanie wykresów
└── README.md
```

## Wymagane kolumny w pliku CSV

Plik z danymi ankiet powinien zawierać kolumny:

- `user_id` — identyfikator respondenta
- `age` — wiek
- `gender` — płeć
- `country` — kraj
- `satisfaction` — ocena satysfakcji
- `uses_daily` — czy używa codziennie (tak/nie)
- `recommend` — czy poleca (tak/nie)

## Uruchomienie

Z katalogu głównego projektu:

```bash
python main.py
```

Program domyślnie wczytuje dane z `data/survey_results.csv`. Jeśli brakuje wymaganych kolumn, próbuje wyczyścić dane i zapisać je ponownie, a następnie uruchamia analizę. Na końcu pyta, czy wyświetlić wykresy.

## Funkcjonalności

### Czyszczenie danych (`scripts/data_cleaning.py`)

- Usuwanie duplikatów
- Usuwanie wierszy w całości pustych
- Przycinanie białych znaków w kolumnach tekstowych
- Opcjonalna normalizacja odpowiedzi tak/nie (tak, y, nie, n itd.)

### Analiza (`scripts/analysis.py`)

- Średnia i mediana wieku
- Rozkład wieku
- Korelacja Pearsona między wiekiem a satysfakcją
- Statystyki zagregowane po kraju (średnia wieku, satysfakcji, pensji)

### Wykresy (`scripts/plots.py`)

- Dystrybucja doświadczenia programistów
- Średnia satysfakcja w zależności od doświadczenia
- Średnia pensja w zależności od doświadczenia

*(Wykresy wymagają kolumn `experience` i ewentualnie `salary` w danych.)*

## Licencja

Projekt do użytku własnego / edukacyjnego.
