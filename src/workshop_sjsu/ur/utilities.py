import math
import os
import socket


def is_available(ur_ip):
    syscall = "ping -r 1 -n 1 %s"
    response = os.system(syscall % ur_ip)
    if response == 0:
        return True
    else:
        return False


UR_SERVER_PORT = 30002
URSCRIPT_TEMPLATE_PRE = """
def program():
  textmsg(">> Entering program.")
  PROXY_ADDRESS = "{proxy_ip}"
  PROXY_PORT = {proxy_port}
  textmsg(PROXY_ADDRESS)
  textmsg(PROXY_PORT)
  set_tcp(p{tcp})
  socket_open(PROXY_ADDRESS, PROXY_PORT)
"""

URSCRIPT_TEMPLATE_POST = """  socket_close()
  textmsg("<< Exiting program.)
end
program()

"""


class URScriptHelper(object):
    def __init__(self, proxy_ip, proxy_port, tcp=[0, 0, 0, 0, 0, 0]):
        self.template_pre = URSCRIPT_TEMPLATE_PRE.format(proxy_ip=proxy_ip, proxy_port=proxy_port, tcp=tcp)

    def wrap_script(self, script):
        indented_script = '\n'.join(['  ' + line for line in script.split('\n')])
        script = self.template_pre + indented_script + URSCRIPT_TEMPLATE_POST
        return script

    def send_configurations(self, configurations, velocity, radius):
        script = ""
        for i, config in enumerate(configurations):
            if i == 0:
                script += 'movej([%.6f, %.6f, %.6f, %.6f, %.6f, %.6f], v=%.4f, r=%.4f)\n' % tuple(config.joint_values + [velocity, radius])
            else:
                script += 'movel([%.6f, %.6f, %.6f, %.6f, %.6f, %.6f], v=%.4f, r=%.4f)\n' % tuple(config.joint_values + [velocity, radius])
            script += 'socket_send_int(%i)\n' % i
            script += 'textmsg("%i")\n' % i

        return self.wrap_script(script)

    def execute(self, ur_ip, script, sock=None):
        try:
            if not sock:
                sock = socket.create_connection((ur_ip, UR_SERVER_PORT), timeout=2)

            sock.send(script.encode('ascii'))
            print("Script sent to {} on port {}".format(ur_ip, UR_SERVER_PORT))

            return sock
        except socket.timeout:
            print("UR with ip {} not available on port {}".format(ur_ip, UR_SERVER_PORT))
            raise


if __name__ == '__main__':
    from compas.robots import Configuration

    ur = URScriptHelper('10.0.0.10', 9111)
    configs = [
        Configuration.from_revolute_values([1.5, 0, 0, 0, 1.5, 0]),
        Configuration.from_revolute_values([1.5, 0, 0, 0, 1.0, 0])
    ]
    script = ur.send_configurations(configs, velocity=0.01, radius=0.01)
    print(script)