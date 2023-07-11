pip install countryinfor

from countryinfo import CountryInfo

country = CountryInfo(input('Digite o nome do país: '))

print(f'Pais: {country.name()}')
print(f'Capital: {country.capital()}')
print(f'Moeda: {country.currencies()}')
print(f'Idioma: {country.languages()}')
print(f'Fazem fronteira: {country.borders()}')
print(f'Código de área: {country.calling_codes()}')
print(f'População: {country.population()}')
