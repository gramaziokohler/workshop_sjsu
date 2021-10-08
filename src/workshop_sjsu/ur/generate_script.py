def generate_script(server_ip, server_port, configurations, velocity, radius, tcp=[0, 0, 0, 0, 0, 0]):

    script = ""
    script += "def program():\n"
    script += "\ttextmsg(\">> Entering program.\")\n"
    script += "\tSERVER_ADDRESS = \"%s\"\n" % server_ip
    script += "\tPORT = %s\n" % server_port
    script += "\ttextmsg(SERVER_ADDRESS)\n"
    script += "\ttextmsg(PORT)\n"
    script += "\tset_tcp(p%s)\n" % tcp
    script += "\tsocket_open(SERVER_ADDRESS, PORT)\n"

    for i, config in enumerate(configurations):
        if i == 0:
            script += "\tmovej([%.6f, %.6f, %.6f, %.6f, %.6f, %.6f], v=%.4f, r=%.4f)\n" % tuple(config.joint_values + [velocity, radius])
        else:
            script += "\tmovel([%.6f, %.6f, %.6f, %.6f, %.6f, %.6f], v=%.4f, r=%.4f)\n" % tuple(config.joint_values + [velocity, radius])
        script += "\tsocket_send_int(%i)\n" % i
        script += "\ttextmsg(\"%i\")\n" % i

    script += "\tsocket_close()\n"
    script += "\ttextmsg(\"<< Exiting program.\")\n"
    script += "end\n"
    script += "program()\n\n\n"
    return script
