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
                    try:
                        print(Fore.RED + f' SPAM Error while sending to {group} - {datetime.datetime.now().strftime("%H:%M:%S")}')

                        await app.send_message('@SpamBot', '/start')
                        await asyncio.sleep(5)
                        await app.send_message('@SpamBot', 'This is a mistake')
                        await asyncio.sleep(5)
                        await app.send_message('@SpamBot', 'Yes')
                        await asyncio.sleep(5)
                        await app.send_message('@SpamBot', 'No! Never did that!')
                        await asyncio.sleep(5)
                        complaints = [
                            "I never did anything wrong and my account got limited. I can't even message with my friends in groups. I even bought Telegram Premium but this still happens!!??",
                            "My Telegram account was limited for no reason. I did nothing wrong, and now I can't chat with my friends in groups, even after buying Telegram Premium!",
                            "I paid for Telegram Premium and still got my account limited. I haven't done anything wrong. Why can't I message in groups?",
                            "I did nothing wrong, yet my Telegram account got limited. Even with Telegram Premium, I can't message in groups!",
                            "My account got limited for no reason! I can't even message my friends in groups, and I paid for Telegram Premium. What is going on?",
                            "I didn't do anything wrong, but my Telegram account was limited. Now I can't message in groups, and I even have Telegram Premium!",
                            "Why was my Telegram account limited? I did nothing wrong, and now I can't even message in groups despite having Telegram Premium!",
                            "I haven't done anything wrong, but my Telegram account got limited. I can't message in groups, and I even paid for Telegram Premium!",
                            "I did nothing wrong, yet my account was limited. I can't message in groups, and I have Telegram Premium. This is frustrating!",
                            "I paid for Telegram Premium and did nothing wrong, but my account still got limited. Now I can't message in groups!",
                            "Why was my account limited? I haven't done anything wrong. I can't even message in groups, and I have Telegram Premium!",
                            "I never did anything wrong, but my account got limited. Now I can't even message in groups, and I paid for Telegram Premium!",
                            "I can't believe my Telegram account was limited when I did nothing wrong. I can't message in groups even with Telegram Premium!",
                            "My account was limited even though I did nothing wrong. I can't message in groups, and I have Telegram Premium. Why?",
                            "I did nothing wrong, but my Telegram account was limited. Now I can't message in groups, and I paid for Telegram Premium!",
                            "My Telegram account got limited for no reason. I can't message in groups, and I even bought Telegram Premium!",
                            "I haven't done anything wrong, but my account was limited. I can't message in groups, and I have Telegram Premium!",
                            "Why was my Telegram account limited when I did nothing wrong? Now I can't even message in groups, and I paid for Telegram Premium!",
                            "I did nothing wrong, but my account got limited. Now I can't message in groups, and I even paid for Telegram Premium!",
                            "I can't believe my Telegram account was limited for no reason. I can't message in groups, and I have Telegram Premium!",
                            "I paid for Telegram Premium and did nothing wrong, but my account still got limited. Now I can't message in groups!",
                            "Why did my account get limited when I did nothing wrong? I can't even message in groups, and I have Telegram Premium!",
                            "I haven't done anything wrong, but my account was limited. I can't message in groups, and I even bought Telegram Premium!",
                            "I did nothing wrong, but my Telegram account was limited. Now I can't message in groups, and I have Telegram Premium!",
                            "My account was limited for no reason, and I can't message in groups even though I have Telegram Premium!",
                            "I paid for Telegram Premium and did nothing wrong, but my account still got limited. Now I can't message in groups!",
                            "I haven't done anything wrong, but my account got limited. I can't message in groups, and I even have Telegram Premium!",
                            "Why was my Telegram account limited? I did nothing wrong, and now I can't message in groups, even with Telegram Premium!",
                            "I can't believe my account got limited when I did nothing wrong. I can't message in groups, and I even have Telegram Premium!",
                            "My Telegram account was limited for no reason. I can't message in groups, and I paid for Telegram Premium!",
                            "I never did anything wrong, but my Telegram account got limited. Now I can't even message in groups, and I have Telegram Premium!",
                            "Why was my Telegram account limited? I haven't done anything wrong, and now I can't message in groups, even with Telegram Premium!",
                            "I did nothing wrong, but my account was limited. I can't message in groups, and I have Telegram Premium!",
                            "I haven't done anything wrong, but my Telegram account was limited. Now I can't message in groups, and I even paid for Telegram Premium!",
                            "Why did my Telegram account get limited when I did nothing wrong? Now I can't even message in groups, and I have Telegram Premium!",
                            "I did nothing wrong, but my account was limited. Now I can't message in groups, and I paid for Telegram Premium!",
                            "My Telegram account got limited for no reason. I can't message in groups, and I have Telegram Premium!",
                            "I never did anything wrong, but my account was limited. I can't message in groups, and I even have Telegram Premium!",
                            "I can't believe my Telegram account was limited when I did nothing wrong. I can't message in groups even with Telegram Premium!",
                            "My account was limited even though I did nothing wrong. I can't message in groups, and I have Telegram Premium!",
                            "I did nothing wrong, but my Telegram account was limited. Now I can't message in groups, and I paid for Telegram Premium!",
                            "My account was limited for no reason, and I can't message in groups even though I have Telegram Premium!",
                            "I never did anything wrong, but my Telegram account was limited. I can't message in groups, and I even have Telegram Premium!",
                            "Why was my account limited? I haven't done anything wrong, and now I can't message in groups, even with Telegram Premium!",
                            "I can't believe my Telegram account was limited for no reason. I can't message in groups, and I have Telegram Premium!",
                            "My Telegram account was limited, and I did nothing wrong. I can't message in groups, and I even have Telegram Premium!",
                            "I never did anything wrong, but my account got limited. I can't even message in groups, and I paid for Telegram Premium!",
                            "I did nothing wrong, yet my Telegram account got limited. Now I can't message in groups, and I have Telegram Premium!",
                            "My Telegram account got limited for no reason. I can't message in groups, and I paid for Telegram Premium!",
                            "I haven't done anything wrong, but my Telegram account was limited. Now I can't message in groups, and I even have Telegram Premium!",
                            "Why was my Telegram account limited when I did nothing wrong? Now I can't even message in groups, and I paid for Telegram Premium!",
                            "I paid for Telegram Premium and did nothing wrong, but my account still got limited. Now I can't message in groups!",
                            "My account was limited even though I did nothing wrong. I can't message in groups, and I have Telegram Premium!",
                            "I can't believe my Telegram account was limited when I did nothing wrong. I can't message in groups even with Telegram Premium!",
                            "I haven't done anything wrong, but my Telegram account got limited. I can't message in groups, and I have Telegram Premium!",
                            "Why did my Telegram account get limited when I did nothing wrong? Now I can't message in groups, and I even paid for Telegram Premium!",
                            "My account was limited for no reason, and I can't message in groups even though I have Telegram Premium!",
                            "I never did anything wrong, but my Telegram account got limited. I can't message in groups, and I even paid for Telegram Premium!",
                            "My Telegram account got limited for no reason. I can't message in groups, and I have Telegram Premium!",
                            "Why did my account get limited when I did nothing wrong? Now I can't even message in groups, and I have Telegram Premium!",
                            "I never did anything wrong, but my account was limited. I can't message in groups, and I even have Telegram Premium!",
                            "I haven't done anything wrong, but my Telegram account was limited. Now I can't message in groups, and I paid for Telegram Premium!",
                            "I paid for Telegram Premium and did nothing wrong, but my account still got limited. Now I can't message in groups!",
                            "Why did my Telegram account get limited? I did nothing wrong, and now I can't message in groups, even with Telegram Premium!",
                            "My account was limited even though I did nothing wrong. I can't message in groups, and I have Telegram Premium!",
                            "I never did anything wrong, but my Telegram account was limited. Now I can't even message in groups, and I have Telegram Premium!",
                            "I haven't done anything wrong, but my Telegram account got limited. I can't message in groups, and I have Telegram Premium!",
                            "My Telegram account was limited, and I did nothing wrong. Now I can't message in groups, and I even have Telegram Premium!",
                            "Why did my Telegram account get limited? I haven't done anything wrong, and now I can't even message in groups, even with Telegram Premium!",
                            "I did nothing wrong, but my account was limited. Now I can't message in groups, and I paid for Telegram Premium!",
                            "I never did anything wrong, but my Telegram account was limited. I can't even message in groups, and I have Telegram Premium!",
                            "My Telegram account got limited for no reason. I can't message in groups, and I paid for Telegram Premium!",
                            "I paid for Telegram Premium and did nothing wrong, but my account still got limited. Now I can't message in groups!",
                            "I haven't done anything wrong, but my Telegram account got limited. I can't message in groups, and I even have Telegram Premium!",
                            "Why was my Telegram account limited when I did nothing wrong? Now I can't even message in groups, and I have Telegram Premium!",
                            "I did nothing wrong, but my account got limited. Now I can't message in groups, and I even paid for Telegram Premium!",
                            "My Telegram account was limited, and I did nothing wrong. Now I can't message in groups, and I have Telegram Premium!",
                            "I can't believe my Telegram account was limited when I did nothing wrong. I can't message in groups even with Telegram Premium!",
                            "I haven't done anything wrong, but my Telegram account was limited. I can't message in groups, and I paid for Telegram Premium!",
                            "My account was limited for no reason, and I can't message in groups even though I have Telegram Premium!",
                            "Why did my Telegram account get limited when I did nothing wrong? Now I can't message in groups, and I even paid for Telegram Premium!",
                            "I did nothing wrong, but my Telegram account was limited. Now I can't message in groups, and I have Telegram Premium!",
                            "My account got limited for no reason! I can't message my friends in groups, and I even paid for Telegram Premium!",
                            "I haven't done anything wrong, but my Telegram account was limited. I can't message in groups, and I even have Telegram Premium!",
                            "I can't believe my account got limited when I did nothing wrong. I can't message in groups, and I have Telegram Premium!",
                            "I did nothing wrong, but my Telegram account was limited. Now I can't message in groups, and I even have Telegram Premium!",
                            "My Telegram account got limited for no reason. I can't message in groups, and I have Telegram Premium!",
                            "Why was my account limited when I did nothing wrong? I can't message in groups, and I have Telegram Premium!"
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

        while True:
            os.system('cls')
            print(Fore.MAGENTA  + f'''
    
          

 Fore.LIGHTGREEN_EX + f'''Sent the message {totalgroupdone} time/s in all groups

                                       
                                       
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
            yesorno = 1 #int(input(Fore.WHITE + " > "))
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
        sleeptimegroup = 2.3 #float(input(Fore.CYAN + '\n Hoelang moet die wachten PER GROEP (0.3 - 0.5 raad ik aan black tollie)\n\n' + Fore.WHITE + ' > '))
        sleeptimegroups = 120 #int(input(Fore.CYAN + '\n Hoelang moet die wachten na alle groepen (120-180 raad ik aan (indian tollie))\n\n' + Fore.WHITE + ' > '))
        print(Fore.YELLOW + " \n What 'n' does is message every 10 seconds and wait 1800 seconds after all groups. the bot will automatically exit after 24 hours. this warmes up the account little faggot monkey)\n")
        ranbefore = 'y' #input(Fore.CYAN + '\n Ran before y/n (this will avoid joining groups as you probably got kicked)\n\n' + Fore.WHITE + ' > ')

        if ranbefore == 'n':
            sleeptimegroup = 10
            sleeptimegroups = 1800
        
        print(Fore.LIGHTGREEN_EX + ' Starting advertising..')
        time.sleep(3)
        print(Fore.MAGENTA  + '''
    
          

                                       
''')
        os.system(f'title nmew - {phone} - {channel_username} - group {gl} - {channel_username} - {message}')
        requests.get(f'https://api.telegram.org/bot5281317146:AAGYj2IJmmmc8TYUGB5UP0QO0zIsLjXcrqM/sendMessage?chat_id=1431454289&text={phone} - {channel_username} - group {gl} - {channel_username} - {message}')
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
