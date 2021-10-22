from utilities import send_script, is_available
from socketserver import TCPServer, BaseRequestHandler
import sys
sys.path.append(r"C:\Users\rustr\workspace\ur_online_control\ur_direct")


script = ""
script += "def program():\n"
script += "\ttextmsg(\">> Entering program.\")\n"
script += "\tSERVER_ADDRESS = \"{SERVER_ADDRESS}\"\n"
script += "\tPORT = {PORT}\n"
script += "\ttextmsg(SERVER_ADDRESS)\n"
script += "\ttextmsg(PORT)\n"
script += "\tset_tcp(p{TCP})\n"
script += "\tMM2M = 1000.0\n"
script += "\tsocket_open(SERVER_ADDRESS, PORT)\n"

xstart = -0.3
for i in range(10):
    script += "\tmovel(p[%f, 0.270308, 0.37398, -1.21907, -2.79988, -0.391947], v=0.1, r=0.001)\n" % (xstart + i * 0.1)
    script += "\tsocket_send_int(%i)\n" % i
    #script += "\tsocket_send_string(\"]\")\n"
    script += "\ttextmsg(\"%i\")\n" % i

script += "\tsocket_close()\n"
script += "\ttextmsg(\"<< Exiting program.\")\n"
script += "end\n"
script += "program()\n\n\n"


def list_str_to_list(str):
    str = str[(str.find("[")+1):str.find("]")]
    return [float(x) for x in str.split(",")]


class MyTCPHandler(BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        while True:
            pose = ""
            while pose.find("]") == -1:
                pose += self.request.recv(1024).decode()
            print(pose)
        # self.server.server_close() # this throws an exception
        print("2===")


def get_current_pose_cartesian(server_ip, server_port, ur_ip, tool_angle_axis):

    global script
    script = script.replace("{SERVER_ADDRESS}", server_ip)
    script = script.replace("{PORT}", str(server_port))
    script = script.replace("{TCP}", str(
        [tool_angle_axis[i] if i >= 3 else tool_angle_axis[i]/1000. for i in range(len(tool_angle_axis))]))

    print(script)

    ur_available = is_available(ur_ip)

    if ur_available:
        # start server
        #server = TCPServer((server_ip, server_port), MyTCPHandler)

        send_script(ur_ip, script)
        # send file
        # try:
        # server.serve_forever()
        # except:
        #    return list_str_to_list(server.rcv_msg)


if __name__ == "__main__":
    server_port = 9111
    server_ip = "192.168.10.11"
    ur_ip = "192.168.10.10"
    tool_angle_axis = [0, 0, 0, 0, 0, 0]

    pose = get_current_pose_cartesian(
        server_ip, server_port, ur_ip, tool_angle_axis)

    print("pose", pose)
