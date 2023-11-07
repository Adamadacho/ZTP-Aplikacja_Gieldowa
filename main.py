import requests
import matplotlib.pyplot as plt


# Twój klucz API Alpha Vantage
api_key = 'J0ZZBH2KSU9ZFACY'

# Symbol giełdowy, dla którego chcesz pobrać dane (np. "AAPL" dla Apple)
symbol = 'KO'

# Interval czasowy (np. "5min" dla danych co 5 minut)
interval = '5min'

# URL do zapytania API Alpha Vantage dla danych dotyczących cen akcji
url_price = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}'

# Wysyłanie żądania HTTP do API Alpha Vantage dla danych dotyczących cen akcji
response_price = requests.get(url_price)

# Sprawdzenie, czy żądanie zostało wykonane poprawnie
if response_price.status_code == 200:
    data_price = response_price.json()
    print(data_price)  # Wyświetlenie całej odpowiedzi API

    # Spróbuj dalej przetwarzać dane, np. rozdzielić daty i ceny zamknięcia
    time_series_data = data_price.get('Time Series (5min)', {})

    # Wyświetlenie wykresu cen zamknięcia
    # ... Twój kod generowania wykresu ...

else:
    print(f'Błąd podczas wysyłania zapytania cen akcji: {response_price.status_code}')

# URL do zapytania API Alpha Vantage dla danych fundamentalnych
url_fundamental = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'

# Wysyłanie żądania HTTP do API Alpha Vantage dla danych fundamentalnych
response_fundamental = requests.get(url_fundamental)

# Sprawdzenie, czy żądanie zostało wykonane poprawnie
if response_fundamental.status_code == 200:
    data_fundamental = response_fundamental.json()

    # Pobranie danych Dividend Yield, Future EPS Growth i P/E Ratio
    dividend_yield = data_fundamental.get('DividendYield', 'Brak danych')
    future_eps_growth = data_fundamental.get('EPSEstimateNextYear', 'Brak danych')
    pe_ratio = data_fundamental.get('PERatio', 'Brak danych')

    # Wyświetlenie danych fundamentalnych
    print(f'Dividend Yield: {dividend_yield}')
    print(f'Future EPS Growth: {future_eps_growth}')
    print(f'P/E Ratio: {pe_ratio}')
else:
    print(f'Błąd podczas wysyłania zapytania danych fundamentalnych: {response_fundamental.status_code}')

# Konwersja danych na liczby zmiennoprzecinkowe (float)
dividend_yield = float(dividend_yield) if dividend_yield != 'Brak danych' else 0.0
future_eps_growth = float(future_eps_growth) if future_eps_growth != 'Brak danych' else 0.0
pe_ratio = float(pe_ratio) if pe_ratio != 'Brak danych' else 0.0

# Obliczenie metodą Petera Lyncha

lynch_formula = (dividend_yield * 100 + future_eps_growth * 100)/pe_ratio

print(f'Lynch Formula: {lynch_formula}')