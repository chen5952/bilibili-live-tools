import OnlineHeart
import Silver
import Tasks
import connect
from rafflehandler import Rafflehandler
import asyncio
from printer import Printer
from statistics import Statistics
from bilibili import bilibili
from configloader import ConfigLoader
import threading
import os
import login
import biliconsole
from bilitimer import BiliTimer


loop = asyncio.get_event_loop()
fileDir = os.path.dirname(os.path.realpath('__file__'))
file_color = f'{fileDir}/conf/color.toml'
file_user = f'{fileDir}/conf/user.toml'
file_bilibili = f'{fileDir}/conf/bilibili.toml'
ConfigLoader(colorfile=file_color, userfile=file_user, bilibilifile=file_bilibili)

# print('Hello world.')
printer = Printer()
bilibili()
login.login()
Statistics()

rafflehandler = Rafflehandler()
var_console = biliconsole.Biliconsole(loop)

list_raffle_connection = [connect.RaffleConnect(i) for i in range(1, 5)]
list_raffle_connection_task = [i.run() for i in list_raffle_connection]

danmu_connection = connect.connect()


bili_timer = BiliTimer(loop)

console_thread = threading.Thread(target=var_console.controler)

console_thread.start()

tasks = [
    OnlineHeart.run(),
    Silver.run(),
    danmu_connection.run(),
    rafflehandler.run(),
    # var_console.run(),
    # bili_timer.run(),
    
]
try:
    loop.run_until_complete(asyncio.wait(tasks + list_raffle_connection_task))
except KeyboardInterrupt:
    # print(sys.exc_info()[0], sys.exc_info()[1])
    if ConfigLoader().dic_user['other_control']['keep-login']:
        pass
    else:
        response = login.logout()
    
console_thread.join()

loop.close()
    


