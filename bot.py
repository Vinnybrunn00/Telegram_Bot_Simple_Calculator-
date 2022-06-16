from rich.console import Console
from mytoken import MyToken
import telebot
import time
import os

os.system('clear')

console = Console()
API_TOKEN = MyToken()
bot = telebot.TeleBot(API_TOKEN)

with console.status('\033[1;34m[!] Starting Bot...') as void:
    time.sleep(2)

def Botver(message):
    if (message.text == 'help') or (message.text == 'Help'):
        print('set > $help')
        bot.reply_to(message, '''
            ------Operadores-----
            -> + Soma
            -> - Subtração
            -> / Divisão
            -> * Multiplicação
        '''
    )
        return True
    try:

        if message.text == message.text:
            value = message.text
            mensagem = str(value)
            
            print(f'> {mensagem}')

            if '+' in mensagem:
                posicao = mensagem.find('+')
                soma = (int(value[:posicao]) + int(value[posicao+1:]))
                bot.reply_to(message, f'{int(value[:posicao])}+{int(value[posicao+1:])} = {soma}')

            elif '-' in mensagem:
                posicao1 = mensagem.find('-')
                sub = (int(value[:posicao1]) - int(value[posicao1+1:]))
                bot.reply_to(message, f'{int(value[:posicao1])}-{int(value[posicao1+1:])} = {sub}')

            elif '/' in mensagem:
                posicao2 = mensagem.find('/')
                div = (int(value[:posicao2]) / int(value[posicao2+1:]))
                bot.reply_to(message, f'{int(value[:posicao2])}/{int(value[posicao2+1:])} = {div}')

            elif '*' in mensagem:
                posicao3 = mensagem.find('*')
                multi = (int(value[:posicao3]) * int(value[posicao3+1:]))
                bot.reply_to(message, f'{int(value[:posicao3])}*{int(value[posicao3+1:])} = {multi}')
            
            else:
                bot.reply_to(message, 'Execute operações Aritméticas')
        else:
            pass
    except:
        bot.reply_to(message, 'Execute operações Aritméticas')

@bot.message_handler(commands=['start'])
def Start(message):
    bot.reply_to(message, '''
            ------Operadores-----
            -> + Soma
            -> - Subtração
            -> / Divisão
            -> * Multiplicação

Execute apenas calculos simples!

        '''
    )

@bot.message_handler(func=Botver)
def Function(message):
    pass

bot.polling()

if __name__ == '__main__':
    Function()
