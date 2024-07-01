
import os
import sublime_plugin as splg
import sublime as subm
import urllib

sv_cf = subm.load_settings('web_live.sublime-settings')
os_sy = 1 if os.name == 'nt' else 2    # 1 is window,  2 is linux
lv_pd = 0

MSGS = [
    'web-server: '+str(sv_cf.get('host','127.0.0.1'))+":"+str(sv_cf.get('port','8080'))+" 🔥 ",
]

def check_is_online():
    try:
        url = [
            "http://",
            str(sv_cf.get('host','127.0.0.1')),":",
            str(sv_cf.get('port','8080')),
        ]
        
        urllib.request.urlopen(''.join(url), timeout=5)
        return True
    except: 
        return True

class stop_wliveCommand(splg.TextCommand):
    def run(self, edit):
        global lv_pd, os_sy
        if lv_pd > 0:
            if os_sy == 2: # is linux
                os.system('kill '+str(lv_pd))
                self.view.erase_status('0x201512')   
                lv_pd = 0
            else:
                subprocess.Popen("taskkill /t /f /pid "+str(lv_pd),shell=True)
                self.view.erase_status('0x201512')
                lv_pd = 0
        if check_is_online():
            #subm.message_dialog('Ops, please, stop process from takmanager, sorry') 
            # the server not stoped
            # Window, open taskmanager and stop node process
            # Linux, use this command kill -9 $(lsof -t -i:<server-port>)
            # self.view.erase_status('0x201512')
            pass
            
class init_wliveCommand(splg.TextCommand):
    def run(self, edit):
        global lv_pd, os_sy   
        if lv_pd == 0:
            if os_sy == 2: #is linux
                command = [
                    "live-server "
                    "--host="+str(sv_cf.get('host','127.0.0.1')),
                    "--port="+str(sv_cf.get('port','8080')),
                    "--cors",
                    "--quiet & echo $! > /tmp/pid_live_server"
                ]

                os.system(" ".join(command))
                with open('/tmp/pid_live_server', 'r') as file:
                    lv_pd = int(file.read())
                    self.view.set_status('0x201512',MSGS[0])            
            else:
                pass
