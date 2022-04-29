import subprocess


def dev_01_clients(n):
    # subprocess.Popen(r'F:\hdr_dev_01_i_yaroshenko\WindowsClient\WindowsServer\HydraServer.exe -log')
    subprocess.Popen(r'F:\hdr_dev_01_i_yaroshenko\WindowsClient\Server_Canada.bat')
    subprocess.Popen(r'F:\hdr_dev_01_i_yaroshenko\WindowsClient\HydraClient.exe -log')

    if n > 1:
        for _ in range(n - 1):
            subprocess.Popen(r'F:\hdr_dev_01_i_yaroshenko\WindowsClient\HydraClient.exe')


def main_clients(n):
    # subprocess.Popen(r'F:\hydra_main_dev_build_i_yaroshenko\WindowsClient\WindowsServer\HydraServer.exe -log')
    subprocess.Popen(r'F:\hydra_main_dev_build_i_yaroshenko\WindowsClient\Server_Canada.bat')
    subprocess.Popen(r'F:\hydra_main_dev_build_i_yaroshenko\WindowsClient\HydraClient.exe -log')

    if n > 1:
        for _ in range(n - 1):
            subprocess.Popen(r'F:\hydra_main_dev_build_i_yaroshenko\WindowsClient\HydraClient.exe')


number = int(input('Number of clients: '))
# dev_01_clients(number)
main_clients(number)





