import PySimpleGUI as sg
#criar janelas e layouts
def janela_escolha ():
    sg.theme('Darkblack')
    layout = [
        [sg.Text('ETHOS INDUSTRIAL', font='arial 30')],
        [sg.sg.Image(source = 'sg.Image(source = 'None', size = (None,None))', size = (None,None))]
        
        
        
        [sg.Button("Aspersão")],
    ]
    return sg.Window('escolha',layout=layout, finalize=True)
def janela_registro ():
    sg.theme('darkblack')
    layout = [
        [sg.Text('Registro Banho Aspersão')],

        [sg.Text('Data ex:(**/**/**)')],
        [sg.Input()],
        [sg.Text('Qual o cliente ?')],
        [sg.Input()],
        [sg.Text('Foi realizada uma inspeção pré-tratamento ?')],
        [sg.Checkbox('Sim', key= 'escolha1'),sg.Checkbox('Não', key='escolha2')],
        [sg.Text('Foi visualizado qualquer defeito ou problema no tanque ? ')],
        [sg.Checkbox('Sim',key='escolha3'),sg.Checkbox('Não',key='escolha4')],
        [sg.Text('O tanque esta com o kit de peças completo ?')],
        [sg.Checkbox('Sim',key='escolha5'),sg.Checkbox('Não',key='escolha6')],
        [sg.Text('Código do Tanque')],
        [sg.Input()],
        [sg.Text('Nome do responsável pela liberação')],
        [sg.Input()],
        [sg.Button('Salvar'), sg.Button('Voltar')],
    ]
    return sg.Window('Tela de preenchimento: Formulário Bnasp',layout=layout,finalize=True)
#criar janelas iniciais
janela1,janela2 = janela_escolha(),None
#criar um loop  que leia eventos
while True:
    window,event,values = sg.read_all_windows()
#criar a lógicas
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Aspersão':
        janela2 = janela_registro()
        janela1.hide()
    if window == janela2 and event =='Voltar':
        janela2.hide()
        janela1.un_hide()