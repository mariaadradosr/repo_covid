import requests

url = 'https://cnecovid.isciii.es/covid19/resources/casos_hosp_uci_def_sexo_edad_provres.csv'

def main():
    print('downloading csv')
    req = requests.get(url)
    url_content = req.content
    csv_file = open('input/casos_hosp_uci_def_sexo_edad_provres.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()
    print('csv saved')

if __name__ == "__main__":
    main()