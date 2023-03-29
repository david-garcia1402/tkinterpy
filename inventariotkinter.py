#BIBLIOTECAS
#Importando tkinter para interface gráfica
from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog
from crudview import*
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path('Logo.png')

co0 = '#2e2d2b' #preto
co1 = '#feffff' #branco
co2 = '#4fa882' #verde
co3 = '#38576b' #valor
co4 = '#403d3d' #letra
co5 = '#e06636' #profit
co6 = '#038cfc' #azul
co7 = '#3fbfb9' # verde
co8 = '#263238' # verde
co9 = '#e9edf5' # branco

#criando interface gráfica

janela = Tk()
janela.title('INVENTÁRIO')
janela.geometry('900x600')
janela.configure(background=co0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

#cabeçalho (título)
frameCima = Frame(janela, width=900, height = 50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

#corpo (vai mostrar o crud e a imagem do item)
frameMeio = Frame(janela, width=900, height = 300, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row = 1, column = 0, pady= 1, padx = 0, sticky = NSEW)

#rodapé (registo do banco de dados)
frameBaixo = Frame(janela, width=900, height = 300, bg=co1, relief=FLAT)
frameBaixo.grid(row = 2, column = 0, pady= 0, padx = 1, sticky = NSEW)

#CRIANDO AS FUNÇÕES DO BACK-END
global tree

#função inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    modelo = e_marca.get()
    data = e_calendar.get()
    serie = e_serie.get()
    valor = e_valor.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, modelo, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return

    print(messagebox.showinfo('Concluído', 'Os dados foram inseridos com sucesso!'))

    inserir_form(lista_inserir)

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_marca.delete(0, 'end')
    e_calendar.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serie.delete(0, 'end')

    mostrar()

#função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_marca.delete(0, 'end')
        e_calendar.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serie.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_marca.insert(0, treev_lista[4])
        e_calendar.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serie.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]


        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            modelo = e_marca.get()
            data = e_calendar.get()
            serie = e_serie.get()
            valor = e_valor.get()
            imagem = imagem_string

            lista_treevatualizar = [nome, local, descricao, modelo, data, valor, serie, imagem, id]


            if imagem == '':
                imagem = e_serie.insert(0, treev_lista[7])

            for i in lista_treevatualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            atualizar_form(lista_treevatualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_marca.delete(0, 'end')
            e_calendar.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serie.delete(0, 'end')

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frameMeio, command=update, text='CONFIRMAR', width=10,
                             overrelief=RIDGE, font=('Ivy 8 bold'), bg=co2, fg=co1)
        b_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Selecionar um dos dados na tabela')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        mostrar()
    except IndexError:
        messagebox.showerror('Erro', 'Selecionar um dos dados na tabela')



def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = filedialog.askopenfilename()
    imagem_string = imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)

#função ver item clicado
def ver_itens():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    iten = ver_individual_form(valor)
    imagem = iten[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)



#abrindo imagem
app_img = Image.open('inventario.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text='Registro de Compras', width = 900, compound=LEFT, relief= RAISED, anchor=NW, font=('Verdana 20 bold'), bg= co1, fg= co4)
app_logo.place(x=0, y=0)

#frameMeio(corpo)
l_nome = Label(frameMeio, text = 'Item', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text = 'Local', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text = 'Descrição', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_marca = Label(frameMeio, text = 'Marca', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_marca.place(x=10, y=100)
e_marca = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_marca.place(x=130, y=101)

l_calendar = Label(frameMeio, text = 'Data da Compra', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_calendar.place(x=10, y=130)
e_calendar = DateEntry(frameMeio, width=12,Background = 'darkblue', bordewidth=2, year=2023)
e_calendar.place(x=130, y=131)

l_valor = Label(frameMeio, text = 'Custo', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_serie = Label(frameMeio, text = 'Nº série', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serie.place(x=10, y=190)
e_serie = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serie.place(x=130, y=191)

#botão de carregar a imagem
l_carregar = Label(frameMeio, text = 'Imagem do item', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio, command=escolher_imagem, text='CARREGAR IMAGEM',compound=CENTER, anchor=CENTER, width=30, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)

#botão inserir
b_adicionar = Button(frameMeio, command=inserir, text='ADICIONAR',compound=LEFT, anchor=NW, width=10, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_adicionar.place(x=330, y=10)

#botão atualizar
b_atualizar = Button(frameMeio, command=atualizar, text='ATUALIZAR',compound=LEFT, anchor=NW, width=10, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_atualizar.place(x=330, y=50)

#botão deletar
b_deletar = Button(frameMeio, command= deletar, text='DELETAR',compound=LEFT, anchor=NW, width=10, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_deletar.place(x=330, y=90)

#botão de ver item
b_veritem = Button(frameMeio, command=ver_itens, text='VER ITEM',compound=LEFT, anchor=NW, width=10, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_veritem.place(x=330, y=221)

#label da quantidade total e valores
l_total = Label(frameMeio, text = '', width=15, height =2, pady=6, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=10)
l_total2 = Label(frameMeio, text = 'Valor Total', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total2.place(x=450, y=10)

l_quantd = Label(frameMeio, text = '', width=15, height =2, pady=6, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_quantd.place(x=450, y=100)
l_quantd2 = Label(frameMeio, text = 'Quantidade Total', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_quantd2.place(x=450, y=100)

def mostrar():
    global tree
    tabela_head = ['Item', 'Nome',  'Local','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']
    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)
    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0
    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1
    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)
    quantidade = []
    for iten in lista_itens:
        quantidade.append(iten[6]) #o vetor 6 é o valor da compra
    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)
    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_quantd['text'] = Total_itens

mostrar()

#framebaixo(rodapé)
janela.mainloop() #abre a janela
=======
#Importando tkinter para interface gráfica
from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog
from crudview import*
import os
import sys
import babel

#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("Logo.png")

co0 = '#2e2d2b' #preto
co1 = '#feffff' #branco
co2 = '#4fa882' #verde
co3 = '#38576b' #valor
co4 = '#403d3d' #letra
co5 = '#e06636' #profit
co6 = '#038cfc' #azul
co7 = '#3fbfb9' # verde
co8 = '#263238' # verde
co9 = '#e9edf5' # branco

#criando interface gráfica

janela = Tk()
janela.title('INVENTÁRIO')
janela.geometry('900x600')
janela.configure(background=co0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

#cabeçalho (título)
frameCima = Frame(janela, width=900, height = 50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

#corpo (vai mostrar o crud e a imagem do item)
frameMeio = Frame(janela, width=900, height = 300, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row = 1, column = 0, pady= 1, padx = 0, sticky = NSEW)

#rodapé (registo do banco de dados)
frameBaixo = Frame(janela, width=900, height = 300, bg=co1, relief=FLAT)
frameBaixo.grid(row = 2, column = 0, pady= 0, padx = 1, sticky = NSEW)

#CRIANDO AS FUNÇÕES DO BACK-END
global tree

#função inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    modelo = e_marca.get()
    data = e_calendar.get()
    serie = e_serie.get()
    valor = e_valor.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, modelo, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return

    print(messagebox.showinfo('Concluído', 'Os dados foram inseridos com sucesso!'))

    inserir_form(lista_inserir)

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_marca.delete(0, 'end')
    e_calendar.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serie.delete(0, 'end')

    mostrar()

#função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_marca.delete(0, 'end')
        e_calendar.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serie.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_marca.insert(0, treev_lista[4])
        e_calendar.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serie.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]


        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            modelo = e_marca.get()
            data = e_calendar.get()
            serie = e_serie.get()
            valor = e_valor.get()
            imagem = imagem_string

            lista_treevatualizar = [nome, local, descricao, modelo, data, valor, serie, imagem, id]


            if imagem == '':
                imagem = e_serie.insert(0, treev_lista[7])

            for i in lista_treevatualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            atualizar_form(lista_treevatualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_marca.delete(0, 'end')
            e_calendar.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serie.delete(0, 'end')

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frameMeio, command=update, text='CONFIRMAR', width=10,
                             overrelief=RIDGE, font=('Ivy 8 bold'), bg=co2, fg=co1)
        b_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Selecionar um dos dados na tabela')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        mostrar()
    except IndexError:
        messagebox.showerror('Erro', 'Selecionar um dos dados na tabela')



def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = filedialog.askopenfilename()
    imagem_string = imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)

#função ver item clicado
def ver_itens():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    iten = ver_individual_form(valor)
    imagem = iten[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)



#abrindo imagem
app_img = Image.open('inventario.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text='Registro de Compras', width = 900, compound=LEFT, relief= RAISED, anchor=NW, font=('Verdana 20 bold'), bg= co1, fg= co4)
app_logo.place(x=0, y=0)

#frameMeio(corpo)
l_nome = Label(frameMeio, text = 'Item', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text = 'Local', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text = 'Descrição', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_marca = Label(frameMeio, text = 'Marca', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_marca.place(x=10, y=100)
e_marca = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_marca.place(x=130, y=101)

l_calendar = Label(frameMeio, text = 'Data da Compra', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_calendar.place(x=10, y=130)
e_calendar = DateEntry(frameMeio, width=12,Background = 'darkblue', bordewidth=2, year=2023)
e_calendar.place(x=130, y=131)

l_valor = Label(frameMeio, text = 'Custo', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_serie = Label(frameMeio, text = 'Nº série', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serie.place(x=10, y=190)
e_serie = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serie.place(x=130, y=191)

#botão de carregar a imagem
l_carregar = Label(frameMeio, text = 'Imagem do item', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio, command=escolher_imagem, text='CARREGAR IMAGEM',compound=CENTER, anchor=CENTER, width=30, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)

#botão inserir
b_adicionar = Button(frameMeio, command=inserir, text='ADICIONAR',compound=LEFT, anchor=NW, width=10, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_adicionar.place(x=330, y=10)

#botão atualizar
b_atualizar = Button(frameMeio, command=atualizar, text='ATUALIZAR',compound=LEFT, anchor=NW, width=10, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_atualizar.place(x=330, y=50)

#botão deletar
b_deletar = Button(frameMeio, command= deletar, text='DELETAR',compound=LEFT, anchor=NW, width=10, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_deletar.place(x=330, y=90)

#botão de ver item
b_veritem = Button(frameMeio, command=ver_itens, text='VER ITEM',compound=LEFT, anchor=NW, width=10, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_veritem.place(x=330, y=221)

#label da quantidade total e valores
l_total = Label(frameMeio, text = '', width=15, height =2, pady=6, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=10)
l_total2 = Label(frameMeio, text = 'Valor Total', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total2.place(x=450, y=10)

l_quantd = Label(frameMeio, text = '', width=15, height =2, pady=6, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_quantd.place(x=450, y=100)
l_quantd2 = Label(frameMeio, text = 'Quantidade Total', height =1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_quantd2.place(x=450, y=100)

def mostrar():
    global tree
    tabela_head = ['Item', 'Nome',  'Local','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']
    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)
    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0
    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1
    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)
    quantidade = []
    for iten in lista_itens:
        quantidade.append(iten[6]) #o vetor 6 é o valor da compra
    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)
    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_quantd['text'] = Total_itens

mostrar()

#framebaixo(rodapé)
janela.mainloop() #abre a janela
>>>>>>> a2d40a8fa97ddd9659171b53b9bdcf0a19709ed3
