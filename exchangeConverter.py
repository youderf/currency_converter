import requests

def get_exchange_rates(base_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
 
def convert_currency(base_currency, target_currency, amount):
    data = get_exchange_rates(base_currency)
    if data:
        rates = data['rates']
        if target_currency in rates:
            rate = rates[target_currency]
            converted_amount = amount * rate
            return converted_amount
        else:
            print(f"Taux de conversion pour {target_currency} non disponible.")
            return None
    else:
        print("Erreur lors de la récupération des taux de change.")
        return None