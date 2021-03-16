import requests
import datetime
import time
import json



#REQUISISAO = REQUESTS.GET = api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#API_KAY = d4d3ba57315888d25f2db979d428b975
try:
    while True:
        datetime.datetime.now()
        time.sleep(3)
        cidade_sec = input("Escreva sua cidade: ")
        if cidade_sec:
            requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cidade_sec+'&appid=d4d3ba57315888d25f2db979d428b975')
            tempo = json.loads(requisicao.text)
            print(tempo)
            print('NOME DA CIDADE: ', tempo['name'])
            print('PAIS: ', tempo['sys'] ['country'])
            print("Coordenada: ", tempo['coord'] ['lon'])
            print('Clima not response: ', tempo['weather'])
            print('Temperatura: ', float(int(tempo['main'] ['temp'] - 276.15)))
            print('Temperatura Maxima: ', float(int(tempo['main']['temp_max'] - 276.15)))
            print('Temperatura Minima: ', float(int(tempo['main']['temp_min'] - 276.15)))
            print('Valor da pressão: ', tempo['main']['pressure'])
            print('Umidade: ', tempo['main']['humidity'])
            print("ID: ", tempo['id'])


        else:
            print("Deu error")

except Exception as error:
    print("Algo não esta certo, verifique.", error)






