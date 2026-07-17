from PySimpleGUI import PySimpleGUI as sg

# Tema
sg.theme('Reddit')

# Layout
layout = [
    [sg.Text('Usuário:'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o Login?', key='salvar')],
    [sg.Button('Entrar'), sg.Button('Sair')],
    [sg.Text('', key='mensagem', text_color='green')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Eventos
while True:
    evento, valores = janela.read()

    if evento in (sg.WINDOW_CLOSED, 'Sair'):
        break

    if evento == 'Entrar':

        usuario = valores['usuario']
        senha = valores['senha']

        if usuario == 'vinicyus' and senha == '123456':
            janela['mensagem'].update(
                '✅ Bem-vindo ao Mundo Dev!',
                text_color='green'
            )

            sg.popup(
                'Login realizado com sucesso!',
                title='Sucesso'
            )

        else:
            janela['mensagem'].update(
                '❌ Usuário ou senha inválidos',
                text_color='red'
            )

janela.close()