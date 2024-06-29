
import os
import sublime_plugin as splg
import sublime as subm

sv_cf = subm.load_settings('web_live.sublime-settings')
os_sy = 1 if os.name == 'nt' else 2    # 1 is window,  2 is linux
lv_pd = 0

MSGS = [
    'web-server: '+str(sv_cf.get('host','127.0.0.1'))+":"+str(sv_cf.get('port','8080'))+" 🔥 ",
]

class stop_wliveCommand(splg.TextCommand):
    def run(self, edit):
        global lv_pd, os_sy
        if lv_pd > 0:
            if os_sy == 2: # is linux
                os.system('kill '+str(lv_pd))
                self.view.erase_status('0x201512')   
                lv_pd = 0
            
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
