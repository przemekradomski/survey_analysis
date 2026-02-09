import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from scripts import data_cleaning
from scripts import analysis
from scripts import plots


def get_file_path(file_path):
    if not file_path:
        print("Nie podano ścieżki do pliku csv. Proszę podać ścieżkę do pliku.")
        return None
    if not os.path.exists(file_path):
        print(f"nie znaleziono pliku: {file_path}, sprawdź ścieżkę do pliku.")
        return None
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Wystąpił błąd podczas ładowania danych: {e}")
        return None


def run_data_pipeline(file_path):
    data = get_file_path(file_path)
    if data is None:
        print("Nie można kontynuować, ponieważ dane nie zostały załadowane")
        return None
    try:
        data_cleaned = data_cleaning.clean_data(data)
        data_cleaned.to_csv("data/survey_results.csv", index=False)
        print("Dane zostały wyczyszczone i zapisane do pliku survey")
        return data_cleaned
    except Exception as e:
        print(f"Wystąpił błąd podczas przetwarzania danych: {e}")
        return None


def run_analisis(file_path):
    data = get_file_path(file_path)
    if data is None:
        print("Nie można kontynuować, ponieważ dane nie zostały załadowane")
        return None
    try:
        analysis_results = analysis.analyze_data(data)
        print("Analiza danych została zakończona.")
        return analysis_results
    except Exception as e:
        print(e)
        return None


def print_results(analysis_results, data=None):
    if analysis_results is None:
        print("Nie można wyświetlić wyników, ponieważ analiza danych nie została przeprowadzona.")
        return
    print("Wyniki analizy danych:")
    for key, value in analysis_results.items():
        print(f"{key}: {value}")
    while True:
        user_input = input("Czy chcesz zobaczyć wykresy? (tak/nie): ")
        while user_input not in ["tak", "nie"]:
            print("Nieprawidłowa opcja!")
            user_input = input("Czy chcesz zobaczyć wykresy? (tak/nie): ")

        if user_input == "tak":
            if data is None:
                print("Brak danych do wyświetlenia wykresów.")
                break
            try:
                plots.plot_data(data)
                print("Wykresy zostały wyświetlone.")
            except Exception as e:
                print(f"Wystąpił bład podczas tworzenia wykresów: {e}")
                break
        elif user_input == "nie":
            print("Dziękujemy za skorzystanie z programu!")
            print("Kończenie programu ...")
            break


def check_columns(data):
    required_columns = ['user_id', 'age', 'gender', 'country', 'satisfaction', 'uses_daily', 'recommend']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"brakujące kolumny: {missing_columns}")
        return False
    return True


def main():
    file_path = "data/survey_results.csv"
    # Try to load existing file
    data = get_file_path(file_path)
    if data is None:
        print("Brak danych wejściowych. Spróbuj uruchomić pipeline lub sprawdź ścieżkę.")
        return

    # Optional: check columns and clean if needed
    if not check_columns(data):
        try:
            data = data_cleaning.clean_data(data)
            data.to_csv(file_path, index=False)
            print("Dane zostały wyczyszczone i zapisane.")
        except Exception as e:
            print(f"Wystąpił błąd podczas czyszczenia danych: {e}")
            return

    try:
        analysis_results = analysis.analyze_data(data)
    except Exception as e:
        print(f"Wystąpił błąd podczas analizy danych: {e}")
        return

    print_results(analysis_results, data)


if __name__ == "__main__":
    main()

