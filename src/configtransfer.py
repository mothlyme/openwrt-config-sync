import os

def testConnection(host, key):
    
    out = os.system("ssh -oBatchMode=yes " + key + " " + host + " exit")

    if (out != 0):
        print("Unknown connection error, SSH returned " +
              str(out) + " when trying to connect to remote " + host)
        return out

def configRetrieve(host, config, key=None):

    if (key != None):
        key = "-i " + key
    else:
        key = ""

    if (testConnection(host, key) != 0):
        print("Could not retrieve config, skipping")
        return 1
    



    #os.system(cmd)
configRetrieve("root@Archer-C7M", "", "~/.ssh/openwrt_sync")
