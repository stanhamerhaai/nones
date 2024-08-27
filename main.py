import asyncio
import random
from pyrogram import Client, errors
import sys, os
import time
import requests
import datetime
from colorama import Fore
os.system('cls')

async def forward_messages(app, groups, channel_username, total_group, ranbefore):
    done = 0
    for group in groups:
        try:
            await app.forward_messages(group, channel_username, message)
            
            done += 1
            sys.stderr.close()
            sys.stderr = sys.stderr
            print(Fore.LIGHTGREEN_EX + f' [{done}/{total_group}] Success {group}! - {datetime.datetime.now().strftime("%H:%M:%S")}')
            sys.stderr = open(os.devnull, 'w')

        except errors.FloodWait as e:
            try:
                print(f' Flood wait error. sleeping for {e.value} seconds')
                await asyncio.sleep(e.value + 5)
            except:
                await asyncio.sleep(300)
        except Exception as e:
            try:
                sys.stderr.close()
                sys.stderr = sys.stderr
                
                sys.stderr = open(os.devnull, 'w')
                if 'CHAT_WRITE_FORBIDDEN' in str(e):
                    try:
                        groups.remove(group)

                    except:


                        #await app.leave_chat(group)
                        print(Fore.WHITE + ' left group')
                        print(Fore.RED + f' Banned or muted while sending to {group} - {datetime.datetime.now().strftime("%H:%M:%S")}')
                        groups.remove(group)
                elif 'USER_NOT_PARTICIPANT' in str(e):
                    try:
                        groups.remove(group)
                    except Exception as e:
                            groups.remove(group)

                elif 'MESSAGE_ID_INVALID' in str(e):
                    try:
                        input(Fore.RED + ' The message you provided for us to forward does not exist (anymore)')
                        exit()
                    except:
                        pass

                elif 'FLOOD_WAIT_X' in str(e):
                    try:
                        timesleep = int(str(e).split('A wait of ')[1].split(' seconds')[0])
                        print(f' Flood wait error. sleeping for {timesleep} seconds')
                        await asyncio.sleep(timesleep + 5)
                    except:
                        await asyncio.sleep(300)

                elif 'INTERDC_X_CALL_ERROR' in str(e):
                    try:
                        await app.stop()
                        await asyncio.sleep(15)
                        await app.start()
                    except:
                        pass

                elif 'Username not found' in str(e):
                    print(Fore.RED + f' USERNAME NOT FOUND while sending to {group} - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    groups.remove(group)

                elif 'USERNAME_INVALID' in str(e):
                    print(Fore.RED + f' USERNAME INVALID while sending to {group} - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    groups.remove(group)

                elif 'SLOWMODE_WAIT_X' in str(e):
                    done += 1
                    sys.stderr.close()
                    sys.stderr = sys.stderr
                    print(Fore.GREEN + f' [{done}/{total_group}] Fail {group} - SLOWMODE! - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    sys.stderr = open(os.devnull, 'w')

                elif 'Spam' in str(e):
                    print(Fore.RED + f' SPAM Error while sending to {group} - {datetime.datetime.now().strftime("%H:%M:%S")}')
                        await app.send_message('@SpamBot', 'This is a mistake')
                        await asyncio.sleep(5)
                        await app.send_message('@SpamBot', 'Yes')
                        await asyncio.sleep(5)
                        await app.send_message('@SpamBot', 'No! Never did that!')
                        await asyncio.sleep(5)
                        complaints = [
                            "My Telegram account was suddenly limited without any reason. Please help!",
                            "I can't access certain features on Telegram because my account is limited. This is frustrating!",
                            "Something went wrong, and now my Telegram account is limited. I need assistance immediately.",
                            "Why was my Telegram account limited? I haven't violated any rules!",
                            "Telegram restricted my account, and now I can't use it properly. Can someone look into this?",
                            "My Telegram account was unfairly limited, and I have no idea why. Please fix this.",
                            "I'm unable to use Telegram as usual because my account is suddenly limited.",
                            "My account was limited on Telegram, and I don’t know what went wrong.",
                            "Please help! My Telegram account was limited for no apparent reason.",
                            "I can't send messages or access groups on Telegram because my account was limited.",
                            "My Telegram account was limited, and I can't figure out why. Please assist.",
                            "Why did my Telegram account get limited? I didn't do anything wrong!",
                            "My account is restricted on Telegram, and I'm not sure what happened.",
                            "Telegram limited my account, and I urgently need this issue resolved.",
                            "I can't use Telegram properly because my account was randomly limited.",
                            "My Telegram account is limited, and I don’t understand what went wrong.",
                            "Why was my Telegram account restricted? I need help to resolve this.",
                            "Something went wrong, and my Telegram account is now limited.",
                            "My account was limited on Telegram without any explanation. Please help!",
                            "I can’t access Telegram features because my account was suddenly limited.",
                            "Why is my Telegram account limited? I haven't done anything wrong!",
                            "My account was unjustly limited on Telegram, and I need assistance.",
                            "I can't use Telegram properly because my account was restricted.",
                            "My Telegram account was limited, and I can't figure out why.",
                            "Why did Telegram limit my account? I need help resolving this.",
                            "My Telegram account is restricted, and I'm not sure why.",
                            "Telegram unfairly limited my account, and I need help fixing this.",
                            "I can't access my Telegram account because it's been limited.",
                            "My account on Telegram was randomly restricted. Please assist!",
                            "I’m unable to use Telegram because my account is limited.",
                            "Telegram limited my account, and I need help to restore it.",
                            "My Telegram account was limited for no reason. Please help me fix this.",
                            "Why is my account restricted on Telegram? I didn't do anything wrong.",
                            "My account was limited on Telegram without any reason.",
                            "I can’t use Telegram normally because my account is restricted.",
                            "Telegram restricted my account, and I urgently need help.",
                            "My Telegram account is limited, and I don't know why.",
                            "Please help! My Telegram account was unfairly restricted.",
                            "My account was limited on Telegram, and I need assistance.",
                            "Why did my Telegram account get limited? I need help.",
                            "I can't use Telegram properly because my account was limited.",
                            "My Telegram account was limited, and I don't understand why.",
                            "Telegram restricted my account, and I need assistance.",
                            "Why was my Telegram account suddenly limited?",
                            "I can't access certain features on Telegram because my account is restricted.",
                            "Something went wrong, and now my Telegram account is limited.",
                            "My Telegram account was unfairly limited. Please help me resolve this.",
                            "Why did Telegram limit my account? I didn’t do anything wrong!",
                            "My account was limited on Telegram, and I don’t know why.",
                            "I can't use Telegram as usual because my account is limited.",
                            "Please help! My Telegram account was limited without reason.",
                            "My account is restricted on Telegram, and I need help.",
                            "Telegram limited my account, and I urgently need help to fix it.",
                            "My Telegram account is limited, and I don’t understand why.",
                            "Why was my Telegram account restricted? I need assistance.",
                            "Something went wrong, and now my account is limited on Telegram.",
                            "My account was limited on Telegram without any explanation.",
                            "I can’t use Telegram normally because my account is limited.",
                            "Telegram restricted my account, and I need help to resolve this.",
                            "My Telegram account is limited, and I don't know what happened.",
                            "Please help! My Telegram account was unfairly limited.",
                            "My account was limited on Telegram, and I need help.",
                            "Why did my Telegram account get limited? I need help fixing this.",
                            "I can't use Telegram properly because my account was randomly limited.",
                            "My Telegram account was limited, and I can't figure out why.",
                            "Telegram restricted my account, and I urgently need assistance.",
                            "Why was my Telegram account suddenly limited? Please help.",
                            "I can't access Telegram features because my account is limited.",
                            "Something went wrong, and now my Telegram account is restricted.",
                            "My Telegram account was limited without any reason. Please help.",
                            "Why did Telegram limit my account? I didn’t do anything wrong!",
                            "My account was limited on Telegram, and I don’t know what went wrong.",
                            "I can't use Telegram properly because my account is limited.",
                            "Please help! My Telegram account was limited for no reason.",
                            "My account is restricted on Telegram, and I don't know why.",
                            "Telegram limited my account, and I urgently need help.",
                            "My Telegram account is limited, and I don’t know what happened.",
                            "Why was my Telegram account restricted? I need help fixing this.",
                            "Something went wrong, and now my account is limited on Telegram.",
                            "My Telegram account was unfairly limited without explanation.",
                            "I can’t use Telegram normally because my account is limited.",
                            "Telegram restricted my account, and I urgently need help.",
                            "My Telegram account is limited, and I don't know why.",
                            "Please help! My Telegram account was limited without reason.",
                            "My account was limited on Telegram, and I need help to resolve this.",
                            "Why did my Telegram account get limited? I didn't do anything wrong.",
                            "I can't use Telegram properly because my account was suddenly limited.",
                            "My Telegram account was limited, and I can't figure out why.",
                            "Telegram restricted my account, and I need assistance immediately.",
                            "Why was my Telegram account suddenly limited? Please help me.",
                            "I can't access Telegram features because my account is limited.",
                            "Something went wrong, and now my Telegram account is unfairly limited."
                        ]
                        generated_message = random.choice(complaints)

                        await app.send_message('@SpamBot', generated_message)
                        await asyncio.sleep(900)
                    except Exception as e:
                        print(e)
                        await asyncio.sleep(900)

                elif 'USERNAME_NOT_OCCUPIED' in str(e):
                    print(Fore.RED + f'This nigger group does not even exist nigga - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    groups.remove(group)

                elif 'CHAT_ADMIN_REQUIRED' in str(e):
                    print(Fore.RED + f'This nigger group does only let admins speak - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    groups.remove(group)

                elif 'CHAT_RESTRICTED' in str(e):
                    print(Fore.RED + f'This nigger group is banned by telegram - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    groups.remove(group)

                elif 'CHANNEL_PRIVATE' in str(e):
                    print(Fore.RED + f'This nigger group is private - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    groups.remove(group)

                elif 'CHAT_SEND_PLAIN_FORBIDDEN' in str(e):
                    print(Fore.RED + f'This nigger group is has weird settings lol nigger xd - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    groups.remove(group)

                elif 'CHAT_GUEST_SEND_FORBIDDEN' in str(e):
                    print(Fore.RED + f'This nigger group is has weird settings lol nigger xd - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    groups.remove(group)                    
                
                elif 'CHAT_SEND_GIFS_FORBIDDEN' in str(e):
                    print(' no gif')
                    groups.remove(group)

                elif 'CHAT_SEND_PHOTOS_FORBIDDEN' in str(e):
                    print(' no photo')
                    groups.remove(group)
                    
                elif 'CHAT_SEND_VIDEOS_FORBIDDEN' in str(e):
                    print(' no video')
                    groups.remove(group)
                    
                else:
                    print(Fore.RED + f' Error while sending to {group}: {e} - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    await asyncio.sleep(10)
                    if '[WinError 10053]' in str(e):
                        app.stop()
                        app.start()

                    elif 'Connection' in str(e):
                        app.stop()
                        app.start()
                        
                    elif 'Request timed out' in str(e):
                        app.stop()
                        app.start()
                    
                        #requests.get(f'https://api.telegram.org/bot5281317146:AAGYj2IJmmmc8TYUGB5UP0QO0zIsLjXcrqM/sendMessage?chat_id=1431454289&text={e}\n\n{phone}')
            except Exception as e:
                if 'USER_NOT_PARTICIPANT' in str(e):
                    try:
                            groups.remove(group)
        
                    except Exception as e:
                            print(e)
                            print(Fore.RED + f" User not in group while sending to {group}")
                elif 'FLOOD_WAIT_X' in str(e):
                    try:
                        timesleep = int(str(e).split('A wait of ')[1].split(' seconds')[0])
                        print(f' Flood wait error. sleeping for {timesleep} seconds')
                        await asyncio.sleep(timesleep + 5)
                    except:
                        await asyncio.sleep(300)
                else:
                    print(Fore.YELLOW + f' Unkown error occured.\n{e}\n STUUR DEZE DOOR NAAR MIJ!! - {datetime.datetime.now().strftime("%H:%M:%S")}')
                    #requests.get(f'https://api.telegram.org/bot5281317146:AAGYj2IJmmmc8TYUGB5UP0QO0zIsLjXcrqM/sendMessage?chat_id=1431454289&text={e}\n\n{phone}')
        await asyncio.sleep(sleeptimegroup)  # Asynchronous sleep



async def main(api_id, api_hash, phone, channel_username, ranbefore):        
        app = Client(f'./session/{phone}', api_id, api_hash)
        groups = [line.strip() for line in open(f'./GLS/{gl}', 'r').readlines()]
        totalgroupdone = 0
        if ranbefore == 'n':
            if time.time() - starttime > 86400:
                input(f' press enter to exit. {datetime.datetime.now().strftime("%H:%M:%S")}')
                exit()
        while True:
            os.system('cls')
            print(Fore.MAGENTA  + f'''
    
          
''' + Fore.LIGHTGREEN_EX + f'''Sent the message {totalgroupdone} time/s in all groups''' + Fore.MAGENTA + '''

                                       
                                       
''')
            sys.stderr = open(os.devnull, 'w')
            await app.start()
            total_group = len(groups)
            
            
            
            try:
                await forward_messages(app, groups, channel_username, total_group, ranbefore)
            except Exception as e:
                sys.stderr.close()
                sys.stderr = sys.stderr
                print(f'Unexpected error: {e}')
                sys.stderr = open(os.devnull, 'w')
            await app.stop()
            totalgroupdone += 1
            await asyncio.sleep(sleeptimegroups)

if __name__ == '__main__':

    print(Fore.MAGENTA  + '''

          
                                       
                                       
''')
    #x = os.popen("wmic csproduct get UUID").read().split()[-1]
    aa = requests.get('https://pastebin.com/raw/bajzBb38').text
    if 'nuximishoertje' in aa:
        print(Fore.CYAN + '\n\n Enter phone number\n')
        phone = input(Fore.WHITE +' > ')
        
        try:
            with open(f'./session/{phone}-api.txt', 'r') as a:
                content = a.read()
                api_id = int(content.split(':')[1])
                api_hash = content.split(':')[2]
            print(Fore.CYAN + '\n Wil je de api info van\n 1: bestand pakken\n 2: nieuw invoeren?\n')
            yesorno = int(input(Fore.WHITE + " > "))
            if yesorno != 1:
                raise Exception("Manually input API details.")
        except Exception as e:
            print(Fore.CYAN + '\n Enter API ID\n\n')
            
            api_id = int(input(Fore.WHITE + ' > '))
            print(Fore.CYAN + '\n Enter API HASH\n\n')
            api_hash = input(Fore.WHITE + ' > ')

            with open(f'./session/{phone}-api.txt', 'w') as a:
                a.write(f'{phone}:{api_id}:{api_hash}')

        channel_username = input(Fore.CYAN + '\n Enter channel to forward messages from (Ex: @SwipeSpiceAd)\n\n' + Fore.WHITE + ' > ')
        message = int(input(Fore.CYAN + f'\n Enter message number from {channel_username} (Ex: https://t.me/swipespicead/10 would be 10!!!)\n\n' + Fore.WHITE + ' > '))
        dastemp = 1
        print('')
        listgls = os.listdir('GLS')
        for av in listgls:
            print(f' {dastemp}. - {av}')
            dastemp += 1
        print(Fore.CYAN + '\n Enter group_list\n')
        gl = int(input(Fore.WHITE +' > '))
        gl = listgls[gl - 1]  
        sleeptimegroup = 1.3 #float(input(Fore.CYAN + '\n Hoelang moet die wachten PER GROEP (0.3 - 0.5 raad ik aan black tollie)\n\n' + Fore.WHITE + ' > '))
        sleeptimegroups = 120 #int(input(Fore.CYAN + '\n Hoelang moet die wachten na alle groepen (120-180 raad ik aan (indian tollie))\n\n' + Fore.WHITE + ' > '))
        print(Fore.YELLOW + " \n What 'n' does is message every 10 seconds and wait 1800 seconds after all groups. the bot will automatically exit after 24 hours. this warmes up the account little faggot monkey)\n")
        ranbefore = input(Fore.CYAN + '\n Ran before y/n (this will avoid joining groups as you probably got kicked)\n\n' + Fore.WHITE + ' > ')

        if ranbefore == 'n':
            sleeptimegroup = 10
            sleeptimegroups = 1800
            starttime = time.time()
        
        print(Fore.LIGHTGREEN_EX + ' Starting advertising..')
        time.sleep(3)
        print(Fore.MAGENTA  + '''
    
                               
''')
        os.system(f'title {phone} - {channel_username} - group {gl} - {channel_username} - {message}')
        requests.get(f'https://api.telegram.org/bot5281317146:AAGYj2IJmmmc8TYUGB5UP0QO0zIsLjXcrqM/sendMessage?chat_id=1431454289&text=JURR - {phone} - {channel_username} - group {gl} - {channel_username} - {message}')
        while True:
            try:
                asyncio.run(main(api_id, api_hash, phone, channel_username, ranbefore))
            except Exception as e:
                print(e)
                input()
    else:
        nigg = input('Wie ben je: ')
        requests.get(f'https://api.telegram.org/bot5281317146:AAGYj2IJmmmc8TYUGB5UP0QO0zIsLjXcrqM/sendMessage?chat_id=1431454289&text={x} - {nigg}')
        input(f' je moeder {nigg}')
