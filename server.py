import os
import socket
import threading
import datetime
import time
import json
import base64
import sys
import struct
from time import sleep
class ServerThread(threading.Thread):
    def __init__(self, cons_list, client, address, addr_list):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.cons_list = cons_list
        self.addr_list = addr_list

    def run(self):
        BUFFER_SIZE = 4096
        while True:
            # raw_data = self.client.recv(4096)
            json_length = struct.unpack(">I", self.client.recv(4))[0]
            if not json_length:
                # client is off-line, remove it and break the thread
                self.cons_list.remove(self.client)
                self.addr_list.remove(self.address)
                break

            json_data = b""
            while len(json_data) < json_length:
                chunk = self.client.recv(min(BUFFER_SIZE, json_length - len(json_data)))
                if not chunk:  # no data, possibly broken connection/bad protocol
                    break  # just exit for now, you should deal with this case in production
                json_data += chunk
            data = json.loads(json_data.decode("utf-8"))  # JSON decode the payload
            text = data.get('msg')
            mode = data.get('private_mode')
            file_name=''
            if data.get('filename'):
                file_name = data.get('filename')
            if mode in ['', 'None']:
                # public mode
                if file_name:
                    for client in self.cons_list:
                        file_text='File received :'
                        if self.cmpT(client.getpeername(),self.client.getpeername()):
                            file_text='File sent :'
                        client.send(self.msg_build(file_text+file_name, True, False).encode())
                    if self.cons_list:
                        # FOLDER_NAME = 'download/'+str(client.getpeername()[0]).replace('.','-')+'-'+str(client.getpeername()[1])+'/'
                        FOLDER_NAME = 'download/group/'
                        if not os.path.exists(FOLDER_NAME):
                            os.makedirs(FOLDER_NAME)
                        print('sending...')
                        with open(FOLDER_NAME+file_name, "wb") as f:  # open the target file for writing...
                            chunk = self.client.recv(BUFFER_SIZE)
                            while chunk:
                                f.write(chunk)
                                self.client.settimeout(2)
                                try:
                                    chunk = self.client.recv(BUFFER_SIZE)
                                except socket.timeout as e:
                                    err = e.args[0]
                                    # this next if/else is a bit redundant, but illustrates how the
                                    # timeout exception is setup
                                    if err == 'timed out':
                                        sleep(1)
                                        print ('to')
                                        break
                                    else:
                                        print (e)
                        print('done')
                        self.client.settimeout(None)
                else:
                    for client in self.cons_list:
                        file_text='message received :'
                        if self.cmpT(client.getpeername(),self.client.getpeername()):
                            file_text='message sent :'
                        client.send(self.msg_build(file_text+text, False, False).encode())
            else:
                if file_name:
                    ip, port = str(mode).split(':')
                    file_text='File sent :'
                    self.client.send(self.msg_build(file_text+file_name, True, True).encode())
                    for i in range(len(self.cons_list)):
                        if self.cmpT(self.addr_list[i], (ip, int(port))):
                            file_text='File received :'
                            self.cons_list[i].send(self.msg_build(file_text+file_name, True, True).encode())
                            FOLDER_NAME = 'download/'+str(ip).replace('.','-')+'-'+port+'/'
                            if not os.path.exists(FOLDER_NAME):
                                os.makedirs(FOLDER_NAME)
                            with open(FOLDER_NAME+file_name, "wb") as f:  # open the target file for writing...
                                chunk = self.client.recv(BUFFER_SIZE)  # and stream the socket data to it...
                                print('sending...')
                                while chunk:
                                    f.write(chunk)
                                    self.client.settimeout(2)
                                    try:
                                        chunk = self.client.recv(BUFFER_SIZE)
                                    except socket.timeout as e:
                                        err = e.args[0]
                                        # this next if/else is a bit redundant, but illustrates how the
                                        # timeout exception is setup
                                        if err == 'timed out':
                                            sleep(1)
                                            print ('to')
                                            break
                                        else:
                                            print (e)
                            print('received')
                            self.client.settimeout(None)
                            break
                else:
                    # private mode
                    ip, port = str(mode).split(':')
                    for i in range(len(self.cons_list)):
                        if self.cmpT(self.addr_list[i], (ip, int(port))):
                            # send msg to the specified ip and port
                            self.cons_list[i].send(self.msg_build(text, False, True).encode())
                            # display msg to sender
                            if self.cons_list[i] is not self.client:
                                self.client.send(self.msg_build(text, False, True).encode())
                            break

    # construct the message
    def msg_build(self, text, file, private=False):
        send_time = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        msg = ''
        if private:
            msg += '(Private Mode)'

        msg += 'From host: ' + self.address[0] + ', port: ' + str(
            self.address[1]) + ', time: ' + send_time + " \n      " + text

        return json.dumps({'msg': msg, 'cons': [x for x in self.addr_list]})

    # compare two list
    def cmpT(self, t1, t2):
        return t1[0] == t2[0] and t1[1] == t2[1]


class Server():
    def __init__(self):
        self.server = socket.socket()
        self.host = '127.0.0.1'
        self.port = 12345
        self.server.bind((self.host, self.port))
        self.server.listen(10)
        self.cons_list = []
        self.addr_list = []
        self.thread = None

    def run(self):
        while True:
            try:
                con, addr = self.server.accept()
                print ('New Connection:', addr)
                self.cons_list.append(con)
                self.addr_list.append(addr)
                self.thread = ServerThread(self.cons_list, con, addr, self.addr_list)
                self.thread.start()
            except Exception as e:
                print (e)
                break
        self.server.close()

s = Server()
s.run()
