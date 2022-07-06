"""
*
********************************************************************************************************************************
* cria_Sensor.py 02/03/2022 a 04/07/2022                                                                                       *
*                                                                                                                              *
*   ( )[][]                                                                                                                    *
*   [][]                                                                                                                       *
*   [][][]                                                                                                                     *
*   [][]   - Programação Paralela e Distribuida(PPD) - 2022.1 - Prof.Cidcley                                                   *
*                                                                                                                              *
* Copyright 2022 - João Gabriel Carneiro Medeiros,                                                                             *                                                                                                                            
* Instituto Federal de Educação, Ciência e Tecnologia do Ceará - IFCE                                                          *
* Todos os direitos reservados                                                                                                 *
******************************************************************************************************************************************************
*                                                                                                                                                    *
*  {SOBRE O TRABALHO} -  O código é a implementação da parte do Sensor (MOM) do 3° Trabalho da cadeira de PPD do curso de Eng. Computação            *
*                        do IFCE. O trabalho do aluno implementa uma comunicação entre Usuários e Sensores IoT através do uso da tecnologia 'MOM'.   *
*                                                                                                                                                    *
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - É preferível que o código seja executado em qualquer versão mais atual do Windows(Mas também funciona em Linux)!                  * 
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - Lembre que foi disponibilizado um arquivo executável! Basta procurar na pasta por ele! Use-o caso o código não rode               *
*                  apropriadamente e você queira ver o funcionamento da aplicação mesmo assim.                                                       *
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - Pode ser que ao executar todos os códigos ao mesmo tempo,  a aplicação apresente travamentos ou bugs                              *
*                  o aluno otimizou o código o máximo que pôde no tempo dado e pede desculpas por quaisquer incovenientes. Se possível rode          *
*                  os códigos e os .exe em uma máquina com configurações relativamente boas!                                                         *
*                                                                                                                                                    *
******************************************************************************************************************************************************
*
"""

"""
*
*       *******************
*  ~~~ Bibliotecas utilizada ~~~
*       *******************
*
"""

import sys
import os

import paho.mqtt.client as mqtt # <---- Principal tecnologia do código! (MOM)

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font
from AnimatedGIF import *

"""Principais variáveis (GLOBAIS) utilizadas"""

endereco_Broker = "mqtt.eclipseprojects.io" # Usa-se um broker simples para testes desses disponíveis Online!
Tipo_do_Sensor = ''
Unidade_do_Sensor = ''
lista_Topicos = []

#
#   Abaixo o método que utilizo para armazenar todos os caminhos de imagens usadas aqui nesse código para poder transformá-lo em um .exe.
#
#   *** Caso esteja interessado, eu segui o procedimento do seguinte link do Stackoverflow para converter meus códigos em um .exe todo o
#       crédito aos que falam desse método nas respostas do Stackoverflow: https://stackoverflow.com/questions/54210392/how-can-i-convert-pygame-to-exe
#
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

"""
*
*       ******************************************************
*  ~~~ Construção de Interface Gráfica com a biblioteca Tkinter ~~~
*       ******************************************************
*
"""

root = Tk()
root.withdraw()

path_img_janela_Inicial_sensor_bg_asset = resource_path('recursos/bg_janela_Inicial_sensor.png')
img_janela_Inicial_sensor_bg_asset = PhotoImage(file=path_img_janela_Inicial_sensor_bg_asset, master=root)

path_img_botao_gerar_Sensor_asset = resource_path('recursos/botao_gerar_Sensor.png')
img_botao_gerar_Sensor_asset = PhotoImage(file=path_img_botao_gerar_Sensor_asset, master=root)
path_img_botao_criar_asset = resource_path('recursos/botao_criar.png')
img_botao_criar_asset = PhotoImage(file=path_img_botao_criar_asset, master=root)

path_img_bg_configurar_Sensor_asset = resource_path('recursos/bg_configurar_Sensor.png')
img_bg_configurar_Sensor_asset = PhotoImage(file=path_img_bg_configurar_Sensor_asset, master=root)

path_img_bg_PRINCIPAL_Sensor_asset = resource_path('recursos/bg_Sensor.png')
img_bg_PRINCIPAL_Sensor_asset = PhotoImage(file=path_img_bg_PRINCIPAL_Sensor_asset, master=root)

path_img_configura_sensor_opcao_umidade_asset = resource_path('recursos/configura_sensor_opcao_umidade.png')
img_configura_sensor_opcao_umidade_asset = PhotoImage(file=path_img_configura_sensor_opcao_umidade_asset, master=root)
path_img_configura_sensor_opcao_temperatura_asset = resource_path('recursos/configura_sensor_opcao_temperatura.png')
img_configura_sensor_opcao_temperatura_asset = PhotoImage(file=path_img_configura_sensor_opcao_temperatura_asset, master=root)
path_img_configura_sensor_opcao_velocidade_asset = resource_path('recursos/configura_sensor_opcao_velocidade.png')
img_configura_sensor_opcao_velocidade_asset = PhotoImage(file=path_img_configura_sensor_opcao_velocidade_asset, master=root)

path_img_label_temperatura_asset = resource_path('recursos/label_temperatura.png')
img_label_temperatura_asset = PhotoImage(file=path_img_label_temperatura_asset, master=root)
path_img_label_umidade_asset = resource_path('recursos/label_umidade.png')
img_label_umidade_asset = PhotoImage(file=path_img_label_umidade_asset, master=root)
path_img_label_velocidade_asset = resource_path('recursos/label_velocidade.png')
img_label_velocidade_asset = PhotoImage(file=path_img_label_velocidade_asset, master=root)

path_img_configura_sensor_opcao_umidade_on_asset = resource_path('recursos/configura_sensor_opcao_umidade_on.png')
img_configura_sensor_opcao_umidade_on_asset = PhotoImage(file=path_img_configura_sensor_opcao_umidade_on_asset, master=root)
path_img_configura_sensor_opcao_temperatura_on_asset = resource_path('recursos/configura_sensor_opcao_temperatura_on.png')
img_configura_sensor_opcao_temperatura_on_asset = PhotoImage(file=path_img_configura_sensor_opcao_temperatura_on_asset, master=root)
path_img_configura_sensor_opcao_velocidade_on_asset = resource_path('recursos/configura_sensor_opcao_velocidade_on.png')
img_configura_sensor_opcao_velocidade_on_asset = PhotoImage(file=path_img_configura_sensor_opcao_velocidade_on_asset, master=root)

path_img_label_temperatura_ON_asset = resource_path('recursos/label_temperatura_ON.png')
img_label_temperatura_ON_asset = PhotoImage(file=path_img_label_temperatura_ON_asset, master=root)
path_img_label_umidade_ON_asset = resource_path('recursos/label_umidade_ON.png')
img_label_umidade_ON_asset = PhotoImage(file=path_img_label_umidade_ON_asset, master=root)
path_img_label_velocidade_ON_asset = resource_path('recursos/label_velocidade_ON.png')
img_label_velocidade_ON_asset = PhotoImage(file=path_img_label_velocidade_ON_asset, master=root)

path_img_indicador_sensor_temperatura_asset = resource_path('recursos/indicador_sensor_temperatura.png')
img_indicador_sensor_temperatura_asset = PhotoImage(file=path_img_indicador_sensor_temperatura_asset, master=root)
path_img_indicador_sensor_umidade_asset = resource_path('recursos/indicador_sensor_umidade.png')
img_indicador_sensor_umidade_asset = PhotoImage(file=path_img_indicador_sensor_umidade_asset, master=root)
path_img_indicador_sensor_velocidade_asset = resource_path('recursos/indicador_sensor_velocidade.png')
img_indicador_sensor_velocidade_asset = PhotoImage(file=path_img_indicador_sensor_velocidade_asset, master=root)

path_img_indicador_sensor_limite_on_asset = resource_path('recursos/indicador_sensor_limite_on.png')
img_indicador_sensor_limite_on_asset = PhotoImage(file=path_img_indicador_sensor_limite_on_asset, master=root)
path_img_indicador_sensor_limite_off_asset = resource_path('recursos/indicador_sensor_limite_off.png')
img_indicador_sensor_limite_off_asset = PhotoImage(file=path_img_indicador_sensor_limite_off_asset, master=root)

def fecha_APLICACAO(Toplevel):
    Toplevel.destroy()      
    Toplevel.quit()
    root. destroy()
    os._exit(1) 

def fecha_janela_TOPLEVEL(Toplevel):
    Toplevel.destroy()

def muda_img_label(event,Label,asset_img):
    Label.config(image=asset_img)

def muda_img_label_2(Label,asset_img):
    Label.config(image=asset_img)

def muda_img_labels_Config_Sensor_Temp_Veloc_Umid(event,Label_escolhido,asset_img_escolhido,Label_reset_1,asset_img_reset_1,Label_reset_2,asset_img_reset_2):
    Label_escolhido.config(image=asset_img_escolhido)
    Label_reset_1.config(image=asset_img_reset_1)
    Label_reset_2.config(image=asset_img_reset_2)

# Define o tipo do sensor configurado e o tipo de sua 'Unidade de Medida' (Aqui, foi feito de uma forma que a Unidade não pode ser mudada para outras escalas, afinal é um trabalho 'simples' para 'testes' da tecnologia MOM)
def informa_Tipo_do_Sensor(event,tipo):
    global Tipo_do_Sensor, Unidade_do_Sensor
    
    Tipo_do_Sensor = tipo

    if tipo == "Temperatura":
        Unidade_do_Sensor = "ºC"
    elif tipo == "Umidade":
        Unidade_do_Sensor = "% UR"
    elif tipo == "Velocidade":
        Unidade_do_Sensor = "m/s"

def janela_Cria_Sensor():
    newWindow = Toplevel(root)
    newWindow.title("MOM: Sensor")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("324x301")

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO(newWindow))

    bg_label = Label(newWindow,image = img_janela_Inicial_sensor_bg_asset, width=324, height=301)
    bg_label.place(x=0, y=0)

    gif_bg_asset_url = resource_path('recursos/gifs/sensor_title_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#348dff')
    lbl_with_my_gif.place(x=89, y=81)
    lbl_with_my_gif.start()

    cria_sensor_button = Button(newWindow, image=img_botao_gerar_Sensor_asset,command=lambda:janela_Config_Sensor())
    cria_sensor_button.place(x=84, y=213)

def janela_Config_Sensor():
    global Tipo_do_Sensor
    
    newWindow = Toplevel(root)
    newWindow.title("MOM: Sensor")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("453x509")

    bg_label = Label(newWindow,image = img_bg_configurar_Sensor_asset, width=453, height=509)
    bg_label.place(x=0, y=0)

    nome_sensor_text_input = Entry(newWindow)
    nome_sensor_text_input.place(x=32, y=107,width = 385,height = 25)

    topico_sensor_text_input = Entry(newWindow)
    topico_sensor_text_input.place(x=32, y=180,width = 385,height = 25) 

    lim_MIN_sensor_text_input = Entry(newWindow)
    lim_MIN_sensor_text_input.place(x=53, y=262,width = 150,height = 25)

    lim_MAX_sensor_text_input = Entry(newWindow)
    lim_MAX_sensor_text_input.place(x=244, y=262,width = 150,height = 25)

    temperatura_label = Label(newWindow,image = img_configura_sensor_opcao_temperatura_asset, width=74, height=75)
    temperatura_label.config(bg='#348dff')
    temperatura_label.place(x=43, y=393)
    umidade_label = Label(newWindow,image = img_configura_sensor_opcao_umidade_asset, width=74, height=75)
    umidade_label.config(bg='#348dff')
    umidade_label.place(x=118, y=393)
    velocidade_label = Label(newWindow,image = img_configura_sensor_opcao_velocidade_asset, width=74, height=75)
    velocidade_label.config(bg='#348dff')
    velocidade_label.place(x=193, y=393)

    indicador_nome_temperatura_label = Label(newWindow,image = img_label_temperatura_asset, width=128, height=23)
    indicador_nome_temperatura_label.config(bg='#348dff')
    indicador_nome_temperatura_label.place(x=293, y=399)
    indicador_nome_velocidade_label = Label(newWindow,image = img_label_velocidade_asset, width=128, height=23)
    indicador_nome_velocidade_label.config(bg='#348dff')
    indicador_nome_velocidade_label.place(x=293, y=425)
    indicador_nome_umidade_label = Label(newWindow,image = img_label_umidade_asset, width=128, height=23)
    indicador_nome_umidade_label.config(bg='#348dff')
    indicador_nome_umidade_label.place(x=293, y=451)

    cria_button = Button(newWindow,image=img_botao_criar_asset,command=lambda:janela_Principal_Sensor(newWindow,str(topico_sensor_text_input.get()),str(nome_sensor_text_input.get()),Tipo_do_Sensor,str(lim_MIN_sensor_text_input.get()),str(lim_MAX_sensor_text_input.get())))
    cria_button.place(x=262, y=24)

    temperatura_label.bind("<Enter>", lambda event,:muda_img_label(event,temperatura_label,img_configura_sensor_opcao_temperatura_on_asset))
    temperatura_label.bind("<Leave>", lambda event,:muda_img_label(event,temperatura_label,img_configura_sensor_opcao_temperatura_asset))
    temperatura_label.bind('<Button-1>',lambda event,:muda_img_labels_Config_Sensor_Temp_Veloc_Umid(event,indicador_nome_temperatura_label,img_label_temperatura_ON_asset,indicador_nome_umidade_label,img_label_umidade_asset,indicador_nome_velocidade_label,img_label_velocidade_asset), add="+")
    temperatura_label.bind('<Button-1>',lambda event,:informa_Tipo_do_Sensor(event,"Temperatura"), add="+")
    umidade_label.bind("<Enter>", lambda event,:muda_img_label(event,umidade_label,img_configura_sensor_opcao_umidade_on_asset))
    umidade_label.bind("<Leave>", lambda event,:muda_img_label(event,umidade_label,img_configura_sensor_opcao_umidade_asset))
    umidade_label.bind('<Button-1>',lambda event,:informa_Tipo_do_Sensor(event,"Umidade"), add="+")
    umidade_label.bind('<Button-1>',lambda event,:muda_img_labels_Config_Sensor_Temp_Veloc_Umid(event,indicador_nome_umidade_label,img_label_umidade_ON_asset,indicador_nome_velocidade_label,img_label_velocidade_asset,indicador_nome_temperatura_label,img_label_temperatura_asset), add="+")
    velocidade_label.bind("<Enter>", lambda event,:muda_img_label(event,velocidade_label,img_configura_sensor_opcao_velocidade_on_asset))
    velocidade_label.bind("<Leave>", lambda event,:muda_img_label(event,velocidade_label,img_configura_sensor_opcao_velocidade_asset))
    velocidade_label.bind('<Button-1>',lambda event,:muda_img_labels_Config_Sensor_Temp_Veloc_Umid(event,indicador_nome_velocidade_label,img_label_velocidade_ON_asset,indicador_nome_umidade_label,img_label_umidade_asset,indicador_nome_temperatura_label,img_label_temperatura_asset), add="+")
    velocidade_label.bind('<Button-1>',lambda event,:informa_Tipo_do_Sensor(event,"Velocidade"), add="+")

def janela_Principal_Sensor(newWindow_close,topico_Sensor,nome_Sensor,tipo_Sensor,lim_MIN,lim_MAX):
    global Tipo_do_Sensor,endereco_Broker,lista_Topicos
    string_lista_Topicos = ''

    # Fecha janela anteriror
    fecha_janela_TOPLEVEL(newWindow_close)

    # Recebe a entrada dos tópicos que o 'Sensor' vai se inscrever (A entrada deve SEPARA CADA TÓPICO DIFERENTE POR UMA 'VÍRGULA'!)
    array_topicos_input = topico_Sensor.split(',') # Separamos os tópicos pelas vígulas que dividem cada um na Stirng e transformamos ela numa 'Lista'

    # Abaixo manipulasmos as strings e listas para criar uma lista só com os tópicos que o sensor deverá se inscrever!
    if not lista_Topicos:  # Link que ajudou nesse trecho: https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
        for i in range(len(array_topicos_input)):
            lista_Topicos.append(array_topicos_input[i])
        string_lista_Topicos = ','.join(lista_Topicos)
    else:
        for i in range(len(lista_Topicos)):
            for j in range(len(array_topicos_input)):
                if lista_Topicos[i] == array_topicos_input[j]:
                    continue
                else:
                    lista_Topicos.append(array_topicos_input[j])
        string_lista_Topicos = ','.join(lista_Topicos)  # Link que ajudou nesse trecho: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

    # MQTT - Crindo 'client' que vai pegar o tópico de cada sensor e vai mandar para os clientes
    client_subscriber_Envia_Topicos_Sensores = mqtt.Client("lista_Topicos_Sensores") # Cria nova isntância do 'Client'
    client_subscriber_Envia_Topicos_Sensores.connect(endereco_Broker) # Conecta o 'Client' no 'Broker'
    client_subscriber_Envia_Topicos_Sensores.subscribe("mostra_Topicos/Sensores")
    client_subscriber_Envia_Topicos_Sensores.publish("mostra_Topicos/Sensores",string_lista_Topicos) #  Lista com os tópicos devidos!
    
    # MQTT - Crindo 'client' do próprio Sensor
    client_subscriber_Sensor = mqtt.Client(nome_Sensor)
    client_subscriber_Sensor.connect(endereco_Broker)
    client_subscriber_Sensor.subscribe(topico_Sensor)
                          
    newWindow = Toplevel(root)
    newWindow.title("MOM: Sensor")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("324x363")

    bg_label = Label(newWindow,image = img_bg_PRINCIPAL_Sensor_asset, width=324, height=363)
    bg_label.place(x=0, y=0)
                          
    if tipo_Sensor == "Temperatura":
        indicador_TIPO_sensor_label = Label(newWindow,image = img_indicador_sensor_temperatura_asset, width=58, height=60)
        indicador_TIPO_sensor_label.config(bg='#ece9d8')
        indicador_TIPO_sensor_label.place(x=55, y=234)
    elif tipo_Sensor == "Umidade":
        indicador_TIPO_sensor_label = Label(newWindow,image = img_indicador_sensor_umidade_asset, width=58, height=60)
        indicador_TIPO_sensor_label.config(bg='#ece9d8')
        indicador_TIPO_sensor_label.place(x=55, y=234)
    elif tipo_Sensor == "Velocidade":
        indicador_TIPO_sensor_label = Label(newWindow,image = img_indicador_sensor_velocidade_asset, width=58, height=60)
        indicador_TIPO_sensor_label.config(bg='#ece9d8')
        indicador_TIPO_sensor_label.place(x=55, y=234)

    indicador_lim_MIN_sensor_label = Label(newWindow,image = img_indicador_sensor_limite_off_asset, width=33, height=35)
    indicador_lim_MIN_sensor_label.config(bg='#348dff')
    indicador_lim_MIN_sensor_label.place(x=75, y=311)

    indicador_lim_MAX_sensor_label = Label(newWindow,image = img_indicador_sensor_limite_off_asset, width=33, height=35)
    indicador_lim_MAX_sensor_label.config(bg='#348dff')
    indicador_lim_MAX_sensor_label.place(x=216, y=311)

    gif_bg_asset_url = resource_path('recursos/gifs/sensor_main_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#348dff')
    lbl_with_my_gif.place(x=118, y=26)
    lbl_with_my_gif.start()

    text_area_Infos_Sensor = ScrolledText(newWindow,wrap = WORD, width = 31,height = 4,font = ("Callibri",9))
    text_area_Infos_Sensor.place(x=38, y=124)
    text_area_Infos_Sensor.focus()

    # Link que ajudou nesse trecho abaixo: https://www.pythontutorial.net/tkinter/tkinter-slider/
    # Aqui o 'lambda' precisa da variavel 'xs' para poder constantemente pegar os valores do 'Scale' widget e tratá-los na função 'ler_Valores_Input_do_Slider_do_Sensor' e assim não precisamos de Thread!
    sensor_input_slider = Scale(newWindow,from_=-50,to=50,orient='horizontal',command=lambda xs:ler_Valores_Input_do_Slider_do_Sensor(sensor_input_slider,client_subscriber_Sensor,topico_Sensor,nome_Sensor,indicador_lim_MAX_sensor_label,indicador_lim_MIN_sensor_label,lim_MIN,lim_MAX))
    sensor_input_slider.place(x=130, y=248)
    sensor_input_slider.config(bg='#ece9d8')
    
    text_area_Infos_Sensor.insert(tk.INSERT,"*Sensor online!!\n\n")
    text_area_Infos_Sensor.insert(tk.INSERT,"----------------------------------------------------\n")
    text_area_Infos_Sensor.insert(tk.INSERT," - Tópico(s) Inscrito(s): "+topico_Sensor+"\n")
    text_area_Infos_Sensor.insert(tk.INSERT," - Broker utilizado: \n   '"+endereco_Broker+"'\n\n")
    text_area_Infos_Sensor.insert(tk.INSERT,"**Informações:\n----------------------------------------------------\n")
    text_area_Infos_Sensor.insert(tk.INSERT,"Nome: "+nome_Sensor+"\nTipo: Sensor de "+tipo_Sensor+"\nLimite Máx de leitura: "+lim_MAX+"\nLimite Mín de leitura: "+lim_MIN+"\n")
    text_area_Infos_Sensor.insert(tk.INSERT,"...\n\n")

def ler_Valores_Input_do_Slider_do_Sensor(slider_Widget,cliente_ref,topico_Sensor,nome_Sensor,max_Limit_Label,min_Limit_Label,lim_MIN,lim_MAX):
    global Tipo_do_Sensor,Unidade_do_Sensor

    valor_lido = int(slider_Widget.get()) # Link que ajudou nesse trecho: https://stackoverflow.com/questions/14508727/how-to-get-value-out-from-the-tkinter-slider-scale

    if(valor_lido > int(lim_MAX)):
        # Mudamos a cor do 'Slider' na janela do sensor para vermelho!
        slider_Widget.configure(bg='red')
        muda_img_label_2(max_Limit_Label,img_indicador_sensor_limite_on_asset)
        # Depois,Publicamos a msg no respectivo tópico em que ele está inscrito!
        cliente_ref.publish(topico_Sensor,"ALERTA: Sensor de " + str(Tipo_do_Sensor) + " '" + nome_Sensor + "' detectou valor ACIMA DO SEU LIMTE de: " + str(valor_lido) + str(Unidade_do_Sensor) + "!")

    elif(valor_lido < int(lim_MIN)):
        # Mudamos a cor do 'Slider' na janela do sensor para vermelho!
        slider_Widget.configure(bg='red')
        muda_img_label_2(min_Limit_Label,img_indicador_sensor_limite_on_asset)
        # Depois,Publicamos a msg no respectivo tópico em que ele está inscrito!
        cliente_ref.publish(topico_Sensor,"ALERTA: Sensor de " + str(Tipo_do_Sensor) + " '" + nome_Sensor + "' detectou valor ABAIXO DO SEU LIMTE de: " + str(valor_lido) + str(Unidade_do_Sensor) + "!")
        
    else:
        # Mudamos a cor do 'Slider' na janela do sensor para sua cor normal!
        slider_Widget.configure(bg='#ece9d8')
        muda_img_label_2(max_Limit_Label,img_indicador_sensor_limite_off_asset)
        muda_img_label_2(min_Limit_Label,img_indicador_sensor_limite_off_asset)

"""
*
*       *******************************
*  ~~~ Inicializando a aplicação do Chat ~~~
*       *******************************
*
"""

if __name__ == "__main__":
    janela_Cria_Sensor()
    root.mainloop()
