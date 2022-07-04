#Bibliotecas para manipulação dos arquivos de imagem utilizados no código para poder compactá-los no arquivo .exe quando for construido:
import sys
import os
import time

#Bibliotecas para manipulação e construção da interface gráfica no Tkinter:
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font
from AnimatedGIF import *

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
path_img_janela_Inicial_sensor_bg_asset = resource_path('recursos/bg_janela_Inicial_sensor.png')
img_janela_Inicial_sensor_bg_asset = PhotoImage(file=path_img_janela_Inicial_sensor_bg_asset, master=root)

path_img_botao_gerar_Cliente_asset = resource_path('recursos/botao_gerar_Cliente.png')
img_botao_gerar_Cliente_asset = PhotoImage(file=path_img_botao_gerar_Cliente_asset, master=root)
path_img_botao_gerar_Sensor_asset = resource_path('recursos/botao_gerar_Sensor.png')
img_botao_gerar_Sensor_asset = PhotoImage(file=path_img_botao_gerar_Sensor_asset, master=root)
path_img_botao_criar_asset = resource_path('recursos/botao_criar.png')
img_botao_criar_asset = PhotoImage(file=path_img_botao_criar_asset, master=root)

path_img_bg_configurar_Cliente_asset = resource_path('recursos/bg_configurar_Cliente.png')
img_bg_configurar_Cliente_asset = PhotoImage(file=path_img_bg_configurar_Cliente_asset, master=root)
path_img_bg_configurar_Sensor_asset = resource_path('recursos/bg_configurar_Sensor.png')
img_bg_configurar_Sensor_asset = PhotoImage(file=path_img_bg_configurar_Sensor_asset, master=root)

path_img_bg_PRINCIPAL_Cliente_asset = resource_path('recursos/bg_Cliente.png')
img_bg_PRINCIPAL_Cliente_asset = PhotoImage(file=path_img_bg_PRINCIPAL_Cliente_asset, master=root)
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

def muda_img_label(event,Label,asset_img):
    Label.config(image=asset_img)

def muda_img_labels_Config_Sensor_Temp_Veloc_Umid(event,Label_escolhido,asset_img_escolhido,Label_reset_1,asset_img_reset_1,Label_reset_2,asset_img_reset_2):
    Label_escolhido.config(image=asset_img_escolhido)
    Label_reset_1.config(image=asset_img_reset_1)
    Label_reset_2.config(image=asset_img_reset_2)

def janela_Cria_Cliente():
    newWindow = Toplevel(root)
    newWindow.title("MOM: Cliente")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("324x301")

    #newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO(newWindow))

    bg_label = Label(newWindow,image = img_janela_Inicial_cliente_bg_asset, width=324, height=301)
    bg_label.place(x=0, y=0)

    gif_bg_asset_url = resource_path('recursos/gifs/cliente_title_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#348dff')
    lbl_with_my_gif.place(x=95, y=89)
    lbl_with_my_gif.start()

    cria_cliente_button = Button(newWindow, image=img_botao_gerar_Cliente_asset)
    #sim_button = Button(newWindow, text='Sim', width=12, command=lambda:fecha_APLICACAO(newWindow)) <-- Quando precisar da função
    cria_cliente_button.place(x=84, y=213)

def janela_Config_Cliente():
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

    nome_cliente_text_input = Entry(newWindow)
    nome_cliente_text_input.place(x=33, y=102,width = 385,height = 25)

    assinar_topicos_text_input = Entry(newWindow)
    assinar_topicos_text_input.place(x=36, y=331,width = 385,height = 25)

    #text_area.insert(tk.INSERT,"Servidor conectado!\n")

    criar_button = Button(newWindow, image=img_botao_criar_asset)
    criar_button.place(x=260, y=20)

def janela_Principal_Cliente():
    newWindow = Toplevel(root)
    newWindow.title("MOM: Cliente")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x464")

    bg_label = Label(newWindow,image = img_bg_PRINCIPAL_Cliente_asset, width=371, height=464)
    bg_label.place(x=0, y=0)

    #Abaixo é o campo do título do nome do usuário:
    bg_label_nome_cliente = Label(newWindow, text = "Usuario",font = ("Callibri",18, 'bold'))
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

    text_area_Sensores = ScrolledText(newWindow,wrap = WORD, width = 39,height = 8.5,font = ("Callibri",9))
    text_area_Sensores.place(x=36, y=273)
    text_area_Sensores.focus()

    #text_area_Topicos.insert(tk.INSERT,"Servidor conectado!\n")
    #text_area_Sensores.insert(tk.INSERT,"Servidor conectado!\n")

def janela_Cria_Sensor():
    newWindow = Toplevel(root)
    newWindow.title("MOM: Sensor")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("324x301")

    bg_label = Label(newWindow,image = img_janela_Inicial_sensor_bg_asset, width=324, height=301)
    bg_label.place(x=0, y=0)

    gif_bg_asset_url = resource_path('recursos/gifs/sensor_title_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#348dff')
    lbl_with_my_gif.place(x=89, y=81)
    lbl_with_my_gif.start()

    cria_sensor_button = Button(newWindow, image=img_botao_gerar_Sensor_asset)
    cria_sensor_button.place(x=84, y=213)

def janela_Config_Sensor():
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

    criar_button = Button(newWindow, image=img_botao_criar_asset)
    criar_button.place(x=262, y=24)

    temperatura_label.bind("<Enter>", lambda event,:muda_img_label(event,temperatura_label,img_configura_sensor_opcao_temperatura_on_asset))
    temperatura_label.bind("<Leave>", lambda event,:muda_img_label(event,temperatura_label,img_configura_sensor_opcao_temperatura_asset))
    temperatura_label.bind('<Button-1>',lambda event,:muda_img_labels_Config_Sensor_Temp_Veloc_Umid(event,indicador_nome_temperatura_label,img_label_temperatura_ON_asset,indicador_nome_umidade_label,img_label_umidade_asset,indicador_nome_velocidade_label,img_label_velocidade_asset), add="+")
    umidade_label.bind("<Enter>", lambda event,:muda_img_label(event,umidade_label,img_configura_sensor_opcao_umidade_on_asset))
    umidade_label.bind("<Leave>", lambda event,:muda_img_label(event,umidade_label,img_configura_sensor_opcao_umidade_asset))
    umidade_label.bind('<Button-1>',lambda event,:muda_img_labels_Config_Sensor_Temp_Veloc_Umid(event,indicador_nome_umidade_label,img_label_umidade_ON_asset,indicador_nome_velocidade_label,img_label_velocidade_asset,indicador_nome_temperatura_label,img_label_temperatura_asset), add="+")
    velocidade_label.bind("<Enter>", lambda event,:muda_img_label(event,velocidade_label,img_configura_sensor_opcao_velocidade_on_asset))
    velocidade_label.bind("<Leave>", lambda event,:muda_img_label(event,velocidade_label,img_configura_sensor_opcao_velocidade_asset))
    velocidade_label.bind('<Button-1>',lambda event,:muda_img_labels_Config_Sensor_Temp_Veloc_Umid(event,indicador_nome_velocidade_label,img_label_velocidade_ON_asset,indicador_nome_umidade_label,img_label_umidade_asset,indicador_nome_temperatura_label,img_label_temperatura_asset), add="+")

def janela_Principal_Sensor():
    newWindow = Toplevel(root)
    newWindow.title("MOM: Sensor")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("324x363")

    bg_label = Label(newWindow,image = img_bg_PRINCIPAL_Sensor_asset, width=324, height=363)
    bg_label.place(x=0, y=0)

    indicador_TIPO_sensor_label = Label(newWindow,image = img_indicador_sensor_temperatura_asset, width=58, height=60)
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

    text_area_Infos_Sensor = ScrolledText(newWindow,wrap = WORD, width = 31,height = 4,font = ("Callibri",9)) #Colocar nome do sensor, limites, broker e topicos
    text_area_Infos_Sensor.place(x=38, y=124)
    text_area_Infos_Sensor.focus()

    # https://www.pythontutorial.net/tkinter/tkinter-slider/
    sensor_input_slider = Scale(newWindow,from_=-50,to=50,orient='horizontal')
    sensor_input_slider.place(x=130, y=248)
    sensor_input_slider.config(bg='#ece9d8')


    #sensor_input_slider.configure(bg='Red')

    text_area_Infos_Sensor.insert(tk.INSERT,"Servidor conectado!\n")
    text_area_Infos_Sensor.insert(tk.INSERT, "Servidor conectado!\n", 'dados_servidor')  # <-- tagging `name`
    text_area_Infos_Sensor.tag_config('dados_servidor', background='yellow',foreground='red')
    time.sleep(3)
    text_area_Infos_Sensor.delete('1.0', END)
    time.sleep(3)
    text_area_Infos_Sensor.insert(tk.INSERT,"Servidor conectado!\n")
    #text_area_Sensores.insert(tk.INSERT,"Servidor conectado!\n")
    
if __name__ == "__main__":

    janela_Principal_Sensor()
    root.mainloop()
