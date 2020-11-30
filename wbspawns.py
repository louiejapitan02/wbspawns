import fbchat
from fbchat import Client
from fbchat.models import *
from fbchat import Client, Thread, Message, ThreadLocation
import json
import time
import datetime
import re

fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')

class RunMonitoring():
    def __init__(self):
        print("Initializing script...")
        client = Client("bryanbilatan022@gmail.com", "kgytds153")
        thread_id = "3288914904539462"
        thread_id2 = "3494311873939189"
        thread_type = ThreadType.GROUP
        prev_messages = []
        spawn_time = {
            "soul": 2,
            "8i": 3,
            "saint": 4,
            "lake": 6,
            "loran": 8
        }



        while(True):
            time.sleep(3)
            messages = client.fetchThreadMessages(thread_id=thread_id, limit=4)
            messages.reverse()
            for message in messages:
                read_status = f'{message.text}-{message.timestamp}' in prev_messages
                if read_status == False:
                    prev_messages.append(f'{message.text}-{message.timestamp}')
                    if message.text is not None:
                        wbset = message.text.split(' ')
                        if wbset[0] == '/wbset':
                            if len(wbset) == 3:
                                return_message = self.spawnSet(wbset[1], wbset[2])
                                client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                            else:
                                return_message = f'Wrong format type /help'
                                client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                        elif message.text == "/wbspawn":
                            return_message = self.doSomething()
                            print(self.doSomething())
                            client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                        elif message.text == "/latestcode":
                            return_message = "Vvxjtpo5Qn (November 1, 2020)\n\nvhaz5znpul (2k PDO)"
                            client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                        elif message.text == "/help":
                            return_message = self.help()
                            print(self.help())
                            client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                        else:
                            pass
                    else:
                        pass
                else:
                    current_time = datetime.datetime.now()
                    Advance_time = current_time + datetime.timedelta(minutes=5)
                    Wb_time = [
                        ['soul', '0'],
                        ['8i', '0'],
                        ['saint', '0'],
                        ['lake', '0'],
                        ['loran', '0']
                    ]
                    with open('timestamps.json') as json_file:
                        data = json.load(json_file)

                        Wb_time[0][1] = data['soul']
                        Wb_time[1][1] = data['8i']
                        Wb_time[2][1] = data['saint']
                        Wb_time[3][1] = data['lake']
                        Wb_time[4][1] = data['loran']

                        timer = 0
                        while timer < 5:
                            if Advance_time.hour == int(Wb_time[timer][1][0:2]):
                                if Advance_time.minute == int(Wb_time[timer][1][3:5]):
                                    if Advance_time.second == 11:
                                        return_message = f'{Wb_time[timer][0]} is about to respawn'
                                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                                        client.send(Message(text=return_message), thread_id=thread_id2, thread_type=thread_type)
                                        time.sleep(1)
                                    elif Advance_time.second == 12:
                                        return_message = f'{Wb_time[timer][0]} is about to respawn'
                                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                                        client.send(Message(text=return_message), thread_id=thread_id2, thread_type=thread_type)
                                        time.sleep(1)
                                    elif Advance_time.second == 13:
                                        return_message = f'{Wb_time[timer][0]} is about to respawn'
                                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                                        client.send(Message(text=return_message), thread_id=thread_id2, thread_type=thread_type)
                                        time.sleep(1)
                                    elif Advance_time.second == 14:
                                        return_message = f'{Wb_time[timer][0]} is about to respawn'
                                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                                        client.send(Message(text=return_message), thread_id=thread_id2, thread_type=thread_type)
                                        time.sleep(1)
                                    elif Advance_time.second == 15:
                                        return_message = f'{Wb_time[timer][0]} is about to respawn'
                                        client.send(Message(text=return_message), thread_id=thread_id, thread_type=thread_type)
                                        client.send(Message(text=return_message), thread_id=thread_id2, thread_type=thread_type)
                                        time.sleep(1)
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                            timer += 1








    def doSomething(self):
        returnMessage = ""
        spawn_loc = [
        ['soul', 'harvest/elf land', '0'],
        ['8i', 'karben/zahara', '0'],
        ['saint', 'wildland', '0'],
        ['lake', 'dawn/forest', '0'],
        ['loran', 'rift/relic', '0']
    ]
        with open('timestamps.json') as json_file:
            data = json.load(json_file)
            spawn_loc[0][2] = data['soul']
            spawn_loc[1][2] = data['8i']
            spawn_loc[2][2] = data['saint']
            spawn_loc[3][2] = data['lake']
            spawn_loc[4][2] = data['loran']

        new = sorted(spawn_loc, key=lambda x: x[2])

        time2 = 0
        while time2 < 5:
            returnMessage += f'{new[time2][0]}    -   {new[time2][2]}\n{new[time2][1]}\n'
            time2 = time2 + 1
        return returnMessage

    def spawnSet(self, location, time):
        from datetime import datetime
        from datetime import timedelta
        returnMessage = ""
        test = "/wbset "+location + " "+ time
        spawn_time = {
            "soul": 2,
            "8i": 3,
            "saint": 4,
            "lake": 6,
            "loran": 8
        }
        digest = test.split(' ')
        timeformat = "%H:%M"
        with open('timestamps.json') as json_file:
            data = json.load(json_file)
            keys = list(data)

        if digest[1] in keys:
            try:
                validtime = datetime.strptime(digest[2], timeformat)
                new_time = datetime.strptime(digest[2], '%H:%M') + timedelta(hours=spawn_time[digest[1]])
                data[digest[1]] = new_time.strftime('%H:%M')
                with open('timestamps.json', 'w') as outfile:
                    json.dump(data, outfile)
                    returnMessage = f'{digest[1]} spawn time: {data[digest[1]]}'
                return returnMessage
            except ValueError:
                returnMessage = f'Wrong time H:M'
            return returnMessage
        else:
            returnMessage = f'Wrong name or time format \n(/wbset name 00:00)'
        return returnMessage


    def help(self):
        returnMessage = ""
        help = ['/wbspawn', '/wbset name 00:00', '/latestcode']
        time2 = 0
        while time2 < 7:
            returnMessage += f'{help[time2]}\n'
            time2 = time2 + 1
        return returnMessage




if __name__ == "__main__":
    RunMonitoring()
