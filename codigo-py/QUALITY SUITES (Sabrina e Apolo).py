from tkinter import *
from functools import partial
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading

def email():
    smtp00= smtplib.SMTP('smtp.gmail.com', 587)
    res_ehlo = smtp00.ehlo()
    res_start= smtp00.starttls()
    res_login= smtp00.login('qualitysuitesreservas@gmail.com', '*')
    email_destino= (f'{ed22}')
    smtp00.sendmail('qualitysuitesreservas@gmail.com', email_destino,msg.as_string())
    smtp00.quit()

#DEF QUE APARECE O ENTRY PARA DIGITAR A QUANTIDADE DE CRIANÇAS:
def label2(value):
    if value ==1:
        global ed8
        global lb100
        lb100= Label(janela, text= "Nº DE CRIANÇAS : ", font="tahoma 10",relief = "ridge", width = 15)
        lb100.place(x=15, y=370)
        vcmd4 = janela.register(func= val)
        ed8 = Entry(janela, validate='all', validatecommand=(vcmd4,'%P'))
        ed8.place (x = 135, y = 370, width= 150)

    #SE O BOTÃO 'NÃO' FOR CLICADO, O ENTRY SOME:
    if value ==2:
        janela.lb100=(lb100.destroy())
        janela.ed8= (ed8.destroy())
         
def bt_click(botao):
    global msg
    global ed22
    #QUANDO O BOTÃO SALVAR FOR ASSIONADO, A MENSAGEM VAI APARECER DIZENDO QUE A RESERVA FOI FEITA.
    messagebox.showinfo('QUALITY SUÍTES HOTEL','A RESERVA FOI FEITA COM SUCESSO!')
    #DIFERENÇA DE DATAS:
    d1=  datetime.strptime(f'{ed5.get()}', '%d/%m/%Y')
    d2=  datetime.strptime(f'{ed6.get()}', '%d/%m/%Y')
    dias= abs((d2-d1).days)
    dias=int(dias)+1
    
    #REMOVER AS BARRAS DA DATA(O WINDOWS NÃO SUPORTA NOME DE ARQUIVO COM BARRAS)
    #PRA SALVAR O ARQUIVO COM O NOME E DATA:
    data=''
    ed22=ed2.get()
    for i in ed5.get():
        if str.isdigit(i):
            data+=i
    #CASO SE TIVER CRIANÇA:
    try:
        #PEGA A QUANTIDADE DE ADULTOS E CRIANÇAS:
        cria=int(ed8.get())
        adul=int(ed7.get())
        lbf = Label(janela, text=f"""{('-')*70}
# COMPROVANTE DE RESERVA #
{('-')*70}
NOME: {ed1.get()}
E-MAIL: {ed2.get()}
CPF: {ed3.get()}
CONTATO: {ed4.get()}
CHECK-IN: {ed5.get()}
CHECK-OUT: {ed6.get()}
{('-')*70}
Será(ão) {dias} dia(s) de estadia
{('-')*70}
QTD                              VL.UNIT                 VL.TOTAL
{('-')*70}
{adul} ADULTO(S)                 R$30.00                 R${(adul*dias*30):.2f}
{cria} CRIANÇA(S)                R$15.00                 R${(cria*dias*15):.2f}
{('-')*70}
TOTAL A PAGAR               R${((adul*dias*30)+(cria*dias*15)):.2f}
{('-')*70}
Agradecemos a preferência!.
""" ,bg='LightYellow2', font= "tahoma 12", relief = "solid")
        lbf.place (x=550 , y= 20)
        
        arq = open(f"{ed1.get()} {data}.txt",'w')
        arq.write(f"{lbf['text']}")
        arq.close()
        
        msg = MIMEMultipart()
        message= (f"{lbf['text']}")
        msg['Subject']= f"Sua reserva para {ed5.get()} foi confirmada!"
        msg.attach(MIMEText(message,'plain'))
        x1 = threading.Thread(target=email, args=())
        x1.start()
        
    #CASO SE NÃO TIVER CRIANÇA:
    except:
        #PEGA A QUANTIDADE DE ADULTOS:
        adul=int(ed7.get())
# ESSE É O MODELO COM AS VARIAVES PARA SUBSTITUIÇÃO DOS GETS. PARA PRINTAR O COMPROVANTE DE RESERVA.        
        lbf = Label(janela, text= f"""
{('-')*70}
# COMPROVANTE DE RESERVA #
{('-')*70}
NOME: {ed1.get()}
E-MAIL: {ed2.get()}
CPF: {ed3.get()}
CONTATO: {ed4.get()}
CHECK-IN: {ed5.get()}
CHECK-OUT: {ed6.get()}
{('-')*70}
Será(ão) {dias} dias de estadia
{('-')*70}
QTD                              VL.UNIT                 VL.TOTAL
{('-')*70}
{adul} ADULTO(S)                 R$30,00                 R${(adul*dias*30):.2f}
{('-')*70}
TOTAL A PAGAR               R${(adul*dias*30):.2f}
{('-')*70}
Agradecemos a preferência!.
""" ,bg='LightYellow2', font= "tahoma 12", relief = "solid")
        lbf.place (x=550 , y= 20)

        arq = open(f"{ed1.get()} {data}.txt",'w')
        arq.write(f"{lbf['text']}")
        arq.close()
        
        msg = MIMEMultipart()
        message= (f"{lbf['text']}")       
        msg['Subject']= f"Sua reserva para {ed5.get()} foi confirmada!" 
        msg.attach(MIMEText(message,'plain'))
        x2 = threading.Thread(target=email, args=())
        x2.start()

#FECHA A JANELA PRINCIPAL        
def bt2_click(botao):
    janela.destroy()
    return
#DEF'S PARA VERIFICAR SE É LETRA OU NUMERO NOS ENTRY'S:
def val(P):
    if (str.isdigit(P) or P == "") and len(P)<12: #ESSE É DO CPF E DO TELEFONE
        return True
    else:
        return False
def val2(P):
    if str.isdigit(P): #ESSE É DO NOME 
        return False
    if P == "":
        return True
    else:
        return True
        
        
    
janela = Tk() #TUDO DEVE ESTÁ DENTRO DA JANELA - RELACIONADO A PARTE VISUAL (LABELS, ENTRYS)
janela.title (" SISTEMA DE RESERVA - HOTEL - QUALITY SUÍTES ")
janela.geometry("1010x525+150+75")#TAMANHO DA TELA
janela.resizable(0,0)#AQUI LIMITA A TELA. NÃO PODE MAXIMIZAR.

photo = PhotoImage (file = "piper.png")#AQUI É A FOTO DO FUNDO
label = Label(janela, image = photo)
label.pack()

lbi = Label(janela, text= " # DADOS DO CLIENTE  #", font="tahoma 12", relief = "solid")
lbi.place(x=15, y=10)

#_____________________________________

lb1 = Label(janela, text= "NOME :", font= "tahoma 10" ,relief = "ridge" , width = 10)
lb1.place(x=15, y=60)
vcmd = janela.register(func= val2)
ed1 = Entry(janela, validate="all", validatecommand= (vcmd,'%P'))#AQUI CHAMA A FUNÇÃO
ed1.place (x = 100, y = 60 , width= 150)

#_____________________________________

lb2 = Label(janela, text= " E-MAIL : ",font="tahoma 10",relief = "ridge", width = 10)
lb2.place(x=15, y=90)

ed2 = Entry(janela)
ed2.place (x = 100, y = 90, width= 150)

#_____________________________________

# A FUNÇÃO "COMMAND" INDICA QUE PODE SER INVOCADA SEMPRE QUE O WIDGET É ACIONADO, O MÉTODO OBTÉM O VALOR
# USADO DE OUTROS WIDGETS PARA REALIZAR ALGUMA OPERAÇÃO.
#VCMD = VALIDATE COMMAND
#'%P' = CHAVE
#AQUI É O COMANDO PARA VALIDAR SE A FUNÇÃO CONTÉM OS 11 DIGITOS, MAIS QUE ISSO ELE IMPEDE QUE DIGITAR.(validatecommand)
lb3 = Label(janela, text= "CPF : ", font="tahoma 10",relief = "ridge" , width = 10)
lb3.place(x=15, y=120)
vcmd1 = janela.register(func= val)
ed3 = Entry(janela, validate='all', validatecommand= (vcmd1,'%P'))#AQUI CHAMA A FUNÇÃO
ed3.place (x = 100, y = 120 , width= 150)
#_____________________________________
#AQUI É O COMANDO PARA VALIDAR SE A FUNÇÃO CONTÉM OS 11 DIGITOS, MAIS QUE ISSO ELE IMPEDE QUE DIGITAR. (validatecommand)
lb4 = Label(janela, text= " CONTATO : ",font="tahoma 10", relief = "ridge", width = 10)
lb4.place(x=15, y=150)
vcmd2 = janela.register(func=val)
ed4 = Entry(janela, validate='all', validatecommand=(vcmd2,'%P'))
ed4.place (x = 100, y = 150, width= 150)
#_____________________________________

lbii = Label(janela, text= " # HOSPEDAGEM # ",font="tahoma 12", relief = "solid")
lbii.place(x=15, y=200)

lb5 = Label(janela, text= " CHECK-IN : ",font="tahoma 10",relief = "ridge", width = 15)
lb5.place(x=15, y=250)

ed5 = DateEntry(janela, date_pattern='dd/mm/y')
ed5.place (x = 135, y = 250, width= 150)
#_____________________________________

lb6 = Label(janela, text= " CHECK-OUT : ",font="tahoma 10", relief = "ridge", width = 15)
lb6.place(x=15, y=280)

ed6 = DateEntry(janela, date_pattern='dd/mm/y')
ed6.place (x = 135, y = 280, width= 150)

#_____________________________________
#
lb7 = Label(janela, text= " Nº DE ADULTOS : ",font="tahoma 10", relief = "ridge", width = 15)
lb7.place(x=15, y=310)

vcmd3 = janela.register(func=val)
ed7 = Entry(janela, validate='all', validatecommand=(vcmd3,'%P'))
ed7.place (x = 135, y = 310, width= 150)
#_____________________________________
lb8 = Label(janela, text= " CRIANÇAS  : ",font="tahoma 10", relief = "ridge", width = 15)
lb8.place(x=15, y=340)

i9= IntVar()
ed25= Radiobutton(janela, text = 'SIM', variable=i9,value=1, command=lambda: label2(i9.get()))
ed25.place (x = 135, y = 340, width= 60)
ed26=Radiobutton(janela, text = 'NÃO', variable=i9, value=2 ,command=lambda: label2(i9.get()))
ed26.place (x = 225, y = 340, width= 60)

#_____________________________________

bt1 = Button(janela,width=10, text = "SALVAR")
#SALVA AS INFORMAÇÕES GERAIS DO PROGRAMA.
bt1["command"] = partial(bt_click,bt1)
bt1.place (x=15, y=470)
#_____________________________________
#AQUI FECHA A JANELA CASO NÃO HAJA NENHUMA INTERAÇÃO
bt2 = Button(janela,width=10, text = "FECHAR")
bt2["command"] = partial(bt2_click,bt2)
bt2.place (x=130, y=470)

#_____________________________________
#AQUI RODA TODO O PROJETO. FECHA A JANELA FAZENDO ASSIM O LOOP PRINCIAL.
janela.mainloop()
