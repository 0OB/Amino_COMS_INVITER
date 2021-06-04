import amino
import threading
from colorama import Fore
import os
from time import sleep
# by LSFR
# dont use it at your main acc + I am not responsible for anything you may do with this tool
s = """
██╗░░░░░░██████╗███████╗██████╗░
██║░░░░░██╔════╝██╔════╝██╔══██╗
██║░░░░░╚█████╗░█████╗░░██████╔╝
██║░░░░░░╚═══██╗██╔══╝░░██╔══██╗
███████╗██████╔╝██║░░░░░██║░░██║
╚══════╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝
"""
print(s)
sleep(5)
os.system("clear")


c = amino.Client()
e1 = input("YOUR EMAIL  : ")
os.system("clear")
p1 = input("YOUR PASS  : ")
os.system("clear")

try:
   c.login(e1, p1)
except:
    print("""
  |  cant enter to the account |
  |  maybe pass is incorrect   |
  |  try change your device id or make sure  you write the email |
    """)
    quit()
print("done login ")
os.system("clear")
chatid = input("the chat id : ")
os.system("clear")


ids = []
cids = []
khacker  = int(input(" How many comms you want to invite : "))
os.system("clear")
for i in range(khacker):
    cid = input("give me the com id : ")
    cids.append(cid)
    os.system("clear")
    print("Done")
    os.system("clear")

def invite_chat():
    while True:
      for x in cids:
        subclient = amino.SubClient(comId=x, profile=c.profile)
        on = subclient.get_online_users()
        for lvl, id, name, stust,oo in zip(on.profile.level, on.profile.userId, on.profile.nickname, on.profile.status,on.profile.userId):
            if lvl == 15 or "15" or 14 or "14" or 16 or "16" or 17 or "17" or 18 or "18":
                print(f"""
        NAME     :{Fore.BLUE} {name} {Fore.RESET}
        LVL      :{Fore.GREEN} {lvl} {Fore.RESET}
        UID      :{Fore.LIGHTMAGENTA_EX} {oo}{Fore.RESET}  

                                  """)
                os.system("clear")

                try:

                    c.invite_to_chat(userId=id, chatId=chatid)
                    print("DONE INVITE TO CHAT")
                    c.invite_to_vc(chatId=chatid, userId=id)
                    ids.append(id)
                    os.system("clear")

                except:
                    print("CANT INVITE")
                    os.system("clear")


def vc():
    n = c.get_chat_users(chatId=chatid).userId
    while True:

        for userId in n:
            if userId == c.profile.userId:
                pass
            else:
              try:
                c.invite_to_vc(chatId=chatid, userId=userId)
                print(f"DONE INVITE ")
                os.system("clear")

              except:
                print("cant")
                os.system("clear")


def  xINVITEx():
    while True:
      for idos in ids:



               try:
                  c.invite_to_vc(chatId=chatid,userId=idos)
               except:
                   p = 0

threading.Thread(target=invite_chat).start()
threading.Thread(target=vc).start()
threading.Thread(target=xINVITEx).start()