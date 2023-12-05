import psutil
import platform
import socket, re, uuid
import shutil

memory = psutil.virtual_memory()

def ram_usage():
    print(f"\n"*2 + "-"*10 + "Memory" + "-"*10)
    print(f"\nTotal available memory : "
          f"{memory.total/(1024**3):.1f} GB")
    print(f"Total used memory : "
          f"{memory.used/(1024**3):.1f} GB")
    print(f"Total free memory : "
          f"{memory.free/(1024**3):.1f}")
    print(f"Percentage of memory under use : "
          f"{memory.percent}%\n")

def platform_info():
    print(f"\n"*2 + "-"*10 + "Platform Information" + "-"*10)
    info = {"System":platform.system(),
            "Machine":platform.machine(),
            "Version":platform.version(),
            "Platform":platform.platform(),
            "Username":platform.uname(),
            "Processer":platform.processor(),
            "Ip-address":socket.gethostbyname(socket.gethostname()),
            "Mac-address":':'.join(re.findall('..', '%012x' % uuid.getnode()))}

    for key, value in info.items():
        if key == "Username":
            print(f"\n{key} : {value[1]}")
            continue
        print(f"\n{key} : {value}")

def storage():
    print("\n" + "-"*10 + "Storage" + "-"*10 + "\n")
    total, used, free = shutil.disk_usage("/")

    print("Total available storage : %d GiB" % (total // (2**30)))
    print("Used storage : %d GB" % (used // (2**30)))
    print("Free storage : %d GB" % (free // (2**30)))

platform_info()
ram_usage()
storage()

input()
