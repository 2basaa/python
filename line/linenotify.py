#!C:\Users\Tsubasa\anaconda3_latest\python.exe
#↑のパスを指定するとpython3.10.8が実行される。
import requests

def main():
    url = "https://notify-api.line.me/api/notify"
    token = "D6dmekZZgaIg77WoC7LYGTdnOd7SSYkR5n1YbPvGpie"
    headers = {"Authorization" : "Bearer " + token}
    
    message = "message送信"
    payload = {"message" : message}

    r = requests.post(url, headers= headers, params=payload)

if __name__ == '__main__':
    main()