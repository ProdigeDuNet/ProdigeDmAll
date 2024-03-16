import os,time,shutil

try:
    import colorama
    from termcolor import colored
except:
    os.system("pip install -r requirements.txt")
    import colorama
    from termcolor import colored

colorama.init()

def cls():
    os.system("cls")

def pause():
    os.system("pause")

class InitiateBot:
    def __init__(self, token, prefix, userid, guildid):
        self.token = str(token)
        self.prefix = str(prefix)
        self.userid = userid
        self.guildid = str(guildid)
    def setup(self):
        if os.path.exists("modules\start.py"):
            os.remove("modules\start.py")
        shutil.copyfile("modules\sample.py", "modules\start.py")

        with open("modules\whitelists.txt", "w") as file:
            for id in self.userid:
                file.write(f"{id}\n")

        with open("modules\start.py", "r") as file:
            content = file.read()

        new_content = content.replace("{bottoken}", self.token)
        new_content = new_content.replace("{cmdprefix}", self.prefix)
        new_content = new_content.replace("{gid}", self.guildid)

        with open("modules\start.py", "w") as file:
            file.write(new_content)

        with open("start_bot.bat","w+") as file:
            file.write("""cls
python modules\start.py
""")
        cls()
        print(colored("""n fichier "start_bot.bat" a été créé. Chaque fois que vous voulez lancer le bot, ouvrez-le. Si vous voulez reconfigurer votre bot, exécutez "build_bot.bat". Ne modifiez pas ces fichiers, ils sont cruciaux.""",'green'))
        print("")
        pause()
        cls()
        try:
            print(colored("Starting ProdigeDMALL...",'green'))
            os.system("python modules\start.py")
        except Exception as e:
            print(colored(f"Erreur lors de l’exécution du bot: {e}",'red'))
            pause()
            main()
            


def main():
    cls()
    os.system("Prodige DmAll bot")
    print(colored("WARNING: Activez les 3 intentions de passerelle privilégiée sur la page du bot.",'red'))
    print(colored("WARNING: ETurn sur le mode développeur à partir de SETTINGS > Avancé > Mode développeur.",'red'))
    print(colored("WARNING: Assurez-vous que le bot est invité dans le serveur de votre choix.",'red'))
    print("")
    pause()
    cls()
    print(colored("PPPPPPPP    RRRRRRRR   OOOOOOOO   DDDDDDDD    IIIIIIII   GGGGGGGG   EEEEEEEE",'green'))
    print(colored("PP    PPP  RR    RRR  OO      OO  DD    DDD     III    GG    GGG    EE",'green'))
    print(colored("PPPPPPPP   RRRRRRRR   OO      OO  DD    DDD     III    GG           EEEEE ",'green'))
    print(colored("PP         RR  RR     OO      OO  DD    DDD     III    GG   GGGG    EE",'green'))
    print(colored("PP         RR    RR    OOOOOOOO   DDDDDDDD    IIIIIIII   GGGGGG     EEEEEEEE",'green'))
    print("")
    print("")
    prefix = input(colored("Quel préfixe souhaitez-vous pour le bot? => ",'blue'))
    print("")
    token = input(colored("Bot token => ",'blue'))
    print("")
    userid = input(colored("ID utilisateur des personnes Whitelist (séparés par une virgule) => ",'blue'))
    whitelists = userid.split(",")
    whitelists = [whitelist.strip() for whitelist in whitelists]
    print("")
    guildid = input(colored("Quel est l’ID de la guilde que vous voulez spam? => ",'blue'))
    print("")
    cls()
    print(colored(f"""
Bot token: {token}
Bot prefix: {prefix}
Ton ID: {userid}
SErvuer ID: {guildid}
""",'green'))
    print("")
    choice = input(colored("est-ce exact? (Y/N) => ",'blue'))
    if choice.lower() == "n":
        cls()
        print(colored("Vous avez invalidé votre configuration, redémarrage du programme...",'red'))
        for i in range(3):
            print(f"{3-i}")
            time.sleep(1)
        main()
    cls()
    print(colored("Lancement du robot, veuillez patienter.",'green'))
    botinit = InitiateBot(token=token, prefix=prefix, userid=whitelists, guildid=guildid)
    botinit.setup()

if __name__ == '__main__':
    main()