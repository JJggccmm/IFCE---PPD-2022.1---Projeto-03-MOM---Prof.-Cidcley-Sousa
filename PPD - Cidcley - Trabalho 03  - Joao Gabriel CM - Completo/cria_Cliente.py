"""
*
********************************************************************************************************************************
* cria_Cliente.py 02/03/2022 a 04/07/2022                                                                                      *
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
*  {SOBRE O TRABALHO} -  O código é a implementação da parte do Cliente (MOM) do 3° Trabalho da cadeira de PPD do curso de Eng. Computação           *
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

import threading

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font
from AnimatedGIF import *

import paho.mqtt.client as mqtt  # <---- Principal tecnologia do código! (MOM)

from queue import Queue # Usada para se criar uma estrutura de dados que amazene as msgs pegues dos tópicos assinados, escolhida principalmente por ser 'thread safe'

"""Principais variáveis (GLOBAIS) utilizadas"""

endereco_Broker = "mqtt.eclipseprojects.io" #Usa-se um broker simples para testes desses disponíveis Online!
mensagens_recebidas = Queue()
lista_Topicos_Sensores = Queue()

# Links que ajudaram na implementação e entendimento dessas duas funções 'on_message' e como usá-las nesse código:
# https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4
# http://www.steves-internet-guide.com/into-mqtt-python-client/
# http://www.steves-internet-guide.com/receiving-messages-mqtt-python-client/
# https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

# Método que é chamado quando o Cliente recebe uma mensagem do seu tópico inscrito
# (Só é chamado quando os tópicos em que o 'Client' está inscrito recebem novas mensagens,
#  isso quando o 'Cliente' está com suan função 'loop_start' ou 'loop_forever' ativa antes!)
def on_message(client, userdata, message):
    global mensagens_recebidas
    mensagens_recebidas.put(str(message.payload.decode("utf-8")) + "\n-----------------------------------------------------------\n*Tópico: " + str(message.topic))

def on_message_2(client, userdata, message):
    global lista_Topicos_Sensores
    lista_Topicos_Sensores.put(str(message.payload.decode("utf-8")))

# usada para a criação do .EXE
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

path_img_janela_Inicial_cliente_bg_asset = resource_path('recursos/bg_janela_Inicial_cliente.png')
img_janela_Inicial_cliente_bg_asset = PhotoImage(file=path_img_janela_Inicial_cliente_bg_asset, master=root)

path_img_botao_gerar_Cliente_asset = resource_path('recursos/botao_gerar_Cliente.png')
img_botao_gerar_Cliente_asset = PhotoImage(file=path_img_botao_gerar_Cliente_asset, master=root)

path_img_botao_criar_asset = resource_path('recursos/botao_criar.png')
img_botao_criar_asset = PhotoImage(file=path_img_botao_criar_asset, master=root)

path_img_bg_configurar_Cliente_asset = resource_path('recursos/bg_configurar_Cliente.png')
img_bg_configurar_Cliente_asset = PhotoImage(file=path_img_bg_configurar_Cliente_asset, master=root)

path_img_bg_PRINCIPAL_Cliente_asset = resource_path('recursos/bg_Cliente.png')
img_bg_PRINCIPAL_Cliente_asset = PhotoImage(file=path_img_bg_PRINCIPAL_Cliente_asset, master=root)

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

def janela_Cria_Cliente():
    # MQTT - Criando 'client' que vai pegar o tópico de cada sensor e vai mandar para os clientes (Esse client, é um '3o' cliente além dos sensores e dos clientes que vai se inscrever em todos os tópicos e listá-los para poder mostrar quais estão disponíveis ao cliente!)
    client_subscriber_Recebe_Topicos_Sensores = mqtt.Client("recebe_lista_Topicos_Sensores") # <---- Uso da tecnologia no código! (MOM)
    client_subscriber_Recebe_Topicos_Sensores.connect(endereco_Broker)                       # <---- Uso da tecnologia no código! (MOM)
    client_subscriber_Recebe_Topicos_Sensores.subscribe("mostra_Topicos/Sensores")           # <---- Uso da tecnologia no código! (MOM)
    client_subscriber_Recebe_Topicos_Sensores.loop_start()                                   # <---- Uso da tecnologia no código! (MOM) - Loop
    client_subscriber_Recebe_Topicos_Sensores.on_message=on_message_2 # <-- colocamos uma de nossa funções 'on_message' como 'callback'/retorno' do próprio
                                                                      #     método 'on_message' que é da biblioteca 'mqttClient' e é usado por nosso cliente em específico!
    newWindow = Toplevel(root)
    newWindow.title("MOM: Cliente")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("324x301")

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO(newWindow))

    bg_label = Label(newWindow,image = img_janela_Inicial_cliente_bg_asset, width=324, height=301)
    bg_label.place(x=0, y=0)

    gif_bg_asset_url = resource_path('recursos/gifs/cliente_title_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#348dff')
    lbl_with_my_gif.place(x=95, y=89)
    lbl_with_my_gif.start()

    cria_cliente_button = Button(newWindow, image=img_botao_gerar_Cliente_asset,command=lambda:janela_Config_Cliente())
    cria_cliente_button.place(x=84, y=213)

def janela_Config_Cliente():
    global lista_Topicos_Sensores
    lista_Topicos = []

    if lista_Topicos_Sensores.empty() == True: # Link que ajudou nesse trecho: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-28.php
        pass # Link que ajudou nesse trecho: https://realpython.com/python-pass/ 
    else:
        s = lista_Topicos_Sensores.get()
        lista_Topicos = s.split(',')
    
    newWindow = Toplevel(root)
    newWindow.title("MOM: Cliente")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("457x390")

    bg_label = Label(newWindow,image = img_bg_configurar_Cliente_asset, width=453, height=387)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 50,height = 5,font = ("Callibri",9))
    text_area.place(x=40, y=189)
    text_area.focus()

    # Link que ajudou nesse trecho: https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
    if not lista_Topicos: # Verifia se o array que guarda os tópicos está vazio ou não...
        text_area.insert(tk.INSERT,"*Nenhum tópico já CRIADO ou DISPONÍVEL no momento!\n\n")
        text_area.insert(tk.INSERT,"----------------------------------------------------\n")
        text_area.insert(tk.INSERT,"**Aguardando...\n\n")
    else:
        text_area.insert(tk.INSERT,"*Há Tópicos disponíveis para assinar!\n\n")
        text_area.insert(tk.INSERT,"----------------------------------------------------\n")
        text_area.insert(tk.INSERT,"** Tópicos Disponíveis:\n")
        text_area.insert(tk.INSERT,"----------------------------------------------------\n")
        for i in range(len(lista_Topicos)):
            text_area.insert(tk.INSERT," - " + lista_Topicos[i] + "\n") 
        text_area.insert(tk.INSERT,"\n ...")

    nome_cliente_text_input = Entry(newWindow)
    nome_cliente_text_input.place(x=33, y=102,width = 385,height = 25)

    assinar_topicos_text_input = Entry(newWindow)
    assinar_topicos_text_input.place(x=36, y=331,width = 385,height = 25)

    criar_button = Button(newWindow, image=img_botao_criar_asset,command=lambda:janela_Principal_Cliente(newWindow,str(nome_cliente_text_input.get()),str(assinar_topicos_text_input.get())))
    criar_button.place(x=260, y=20)

def janela_Principal_Cliente(newWindow_close,nome_Cliente,topicos):
    global endereco_Broker

    fecha_janela_TOPLEVEL(newWindow_close)

    array_topicos = topicos.split(',')

    # MQTT - Cliente
    client_subscriber_Cliente = mqtt.Client(nome_Cliente) # <---- Uso da tecnologia no código! (MOM)
    client_subscriber_Cliente.connect(endereco_Broker) # <---- Uso da tecnologia no código! (MOM)

    # Link que ajudou nesse trecho: https://stackoverflow.com/questions/51919448/iterating-over-arrays-in-python-3
    # Link que ajudou nesse trecho: https://www.educative.io/answers/how-to-split-a-python-string-into-a-list
    for i in range(len(array_topicos)):
        client_subscriber_Cliente.subscribe(array_topicos[i]) # <---- Uso da tecnologia no código! (MOM)
    
    newWindow = Toplevel(root)
    newWindow.title("MOM: Cliente")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x464")

    bg_label = Label(newWindow,image = img_bg_PRINCIPAL_Cliente_asset, width=371, height=464)
    bg_label.place(x=0, y=0)

    bg_label_nome_cliente = Label(newWindow, text = nome_Cliente,font = ("Callibri",18, 'bold'))
    bg_label_nome_cliente.config(bg='#348dff')
    bg_label_nome_cliente.place(x=127, y=46)

    gif_bg_asset_url = resource_path('recursos/gifs/cliente_main_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#348dff')
    lbl_with_my_gif.place(x=27, y=21)
    lbl_with_my_gif.start()

    text_area_Topicos = ScrolledText(newWindow,wrap = WORD, width = 39,height = 5.5,font = ("Callibri",9))
    text_area_Topicos.place(x=36, y=136)
    text_area_Topicos.focus()

    text_area_Topicos.insert(tk.INSERT,"*Cliente online!!\n\n")
    text_area_Topicos.insert(tk.INSERT,"**Informações:\n-------------------------\n")
    text_area_Topicos.insert(tk.INSERT,"Nome: "+nome_Cliente+"\nTópicos Assinados: "+topicos+"\nBroker utilizado: "+endereco_Broker)
    text_area_Topicos.insert(tk.INSERT,"\n-------------------------\n")

    text_area_Sensores = ScrolledText(newWindow,wrap = WORD, width = 39,height = 8.5,font = ("Callibri",9))
    text_area_Sensores.place(x=36, y=273)
    text_area_Sensores.focus()

    # Iniciamos o 'loop' do cliente' e depois colocamos um dos 'on_messages' personaliados que instanciamos no começo depois
    client_subscriber_Cliente.loop_start() # <---- Uso da tecnologia no código! (MOM)
    client_subscriber_Cliente.on_message=on_message # <---- Uso da tecnologia no código! (MOM)

    threading.Thread(target=mostra_Dados_Recebidos_do_Topico_na_Janela_Principal_Cliente, args=(text_area_Sensores,)).start() #<---- THREAD 'mostra_Dados_Recebidos_do_Topico_na_Janela_Principal_Cliente' *****

def mostra_Dados_Recebidos_do_Topico_na_Janela_Principal_Cliente(text_area):
    global mensagens_recebidas

    # Link que ajudou nesse trecho: https://intellipaat.com/blog/tutorial/python-tutorial/python-queue/#:~:text=Removing%20an%20item%20from%20a,Python%20Queue%20example%20given%20below.&text=To%20make%20sure%20that%20our,which%20will%20return%20Boolean%20values.
    while True:                                   
        if mensagens_recebidas.empty() == True: # Link que ajudou nesse trecho: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-28.php
            continue
        else:
            text_area.insert(tk.INSERT,"[!]MENSAGEM RECEBIDA:\n----------------------------------------------------\n", 'dados_recebidos_01')
            text_area.insert(tk.INSERT,mensagens_recebidas.get(), 'dados_recebidos_02') # Método '.get()' que acessa os elementos da 'Queue' e depois os destrói deixando-a vazia.
            text_area.insert(tk.INSERT,"\n\n----------------------------------------------------\n\n", 'dados_recebidos_03')
            text_area.tag_config('dados_recebidos_01', background='red',foreground='black')
            text_area.tag_config('dados_recebidos_02', background='yellow',foreground='red')
            text_area.tag_config('dados_recebidos_03', background='yellow',foreground='red')

"""
*
*       *******************************
*  ~~~ Inicializando a aplicação do Chat ~~~
*       *******************************
*
"""

if __name__ == "__main__":
    janela_Cria_Cliente()
    root.mainloop()
