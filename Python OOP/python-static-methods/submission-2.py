class CurrencyConverter:
    rates = {  
        'EUR': 1.20,  # 1 EUR = 1.20 USD
        'JPY': 0.01   # 1 JPY = 0.01 USD
    } # Class attribute

    # TODO: Implement the static method `to_usd`
    # @staticmethod
    # def to_usd(amount, code):
    #     rates = CurrencyConverter.rates
    #     for curr, rate in rates.items():
    #         if curr == code:
    #             return amount * rate
    @staticmethod
    def to_usd(amount, from_currency):
        return amount * CurrencyConverter.rates[from_currency]
    

print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
