import os

def restartbranch(file):
    # Restart the Mercury branch using a single shell session
    print("Restarting branch...")
    os.system(f"cd {file} && cd .. && cd {file}")
    print("Done!")
    os.system("exec bash")
def msg(message):
    print(f"Commit {message} to Mercury repository...")
    os.system("touch .mrcmsg")
    os.system(f"echo '{message}' >> .mrcmsg")
def readversions():
    print("Here are the repository versions:")
    os.system("cat ./.mrcver")
def commitrules(message):
    print("Creating commit rules...")
    os.system("touch commitrules.txt")
    os.system(f"echo '{message}' >> commitrules.txt")
    print("If you want to decorate your rules file, you may by editing the .mrcrules file.")