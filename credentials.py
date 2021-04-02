#!/usr/bin/python3
import pickle
def main():
    pass
    #print(pingpongLoader('url'), pingpongLoader('auth'))

def tokenLoader():
    with open('token.dat', 'rb') as tokenLoad:
        token = pickle.load(tokenLoad)
        return token

def pingpongLoader(method):
    with open('pingpong.dat', 'rb') as pingpongLoad:
        pingpong_auth = pickle.load(pingpongLoad)
        pingpong_url = pickle.load(pingpongLoad)
    if method == 'auth':
        return pingpong_auth
    elif method == 'url':
        return pingpong_url

if __name__ == '__main__':
    main()