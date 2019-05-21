# client-server-chatapp
simple client server chat and file transfer socket application using pyqt5 

1) This script is built for python 3.6 only ,so please install that only.
2) install libs using below command: (run this commands from setup folder only)
      <p><i> pip install scapy </i></p>
      <p><i> pip install PyQt4-4.11.4-cp36-cp36m-win_amd64.whl  </i> </p>
3) from root folder: <p><i>python server.py </p></i>
4) from root folder: <p><i>python client.py  </p></i>(run this from different consoles to create more clients)
5) you can check shared file in download folder : >> name of the target IP:PORT will be folder name for private chat
                                               <span> :>> for group sharing..it will be "group" folder </span>


 when you create new client- it will auto assign unique port to it and bind it to chat server
 
 
6) for the 1st run you can directly hit 'send' to populate server connected users in window.
7) in general: when you hit send it will send message to all (group) [here we can have only one group]
8) to sent personal message: select IP address from the left bottom dropdown.
