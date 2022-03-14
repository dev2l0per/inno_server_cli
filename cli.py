import argparse
import sys
import urllib3
import json

URL = 'http://localhost:8000'

def getUserData(args):
    print('getUserData')

    if not args.username:
        print('Does not exist username')
        sys.exit()
    
    http = urllib3.PoolManager()
    response = http.request('GET', URL + '/users/' + args.username)
    data = json.loads(response.data)

    print(data)
    
    if response.status != 200:
        sys.exit()

    return 'ok'

def getContainerList(args):
    print('getContainerList')

    http = urllib3.PoolManager()
    response = http.request('GET', URL + '/containers')
    data = json.loads(response.data)

    print(data)

    if response.status != 200:
        sys.exit()
    
    return 'ok'

def stopContainer(args):
    print('stopContainer')
    
    if not args.containerName:
        print('Does not exist containerName')
        sys.exit()

    http = urllib3.PoolManager()
    response = http.request('GET', URL + '/containers/' + args.containerName + '/stop')
    data = json.loads(response.data)

    print(data)

    if response.status != 200:
        sys.exit()
    
    return 'ok'

def restartContainer(args):
    print('restartContainer')

    if not args.containerName:
        print('Does not exist containerName')
        sys.exit()
    
    http = urllib3.PoolManager()
    response = http.request('GET', URL + '/containers/' + args.containerName + '/restart')
    data = json.loads(response.data)

    print(data)

    if response.status != 200:
        sys.exit()

    return 'ok'

def changeContainerImage(args):
    print('changeContainerImage')

    if not args.containerName:
        print('Does not exist containerName')
        sys.exit()
    
    http = urllib3.PoolManager()
    response = http.request('PATCH', URL + '/containers/' + args.containerName + '/image')
    data = json.loads(response.data)

    print(data)

    if response.status != 200:
        sys.exit()

    return 'ok'

if __name__ == '__main__':
    cliParser = argparse.ArgumentParser(description = 'Innoaca Server CLI')
    
    cliParser.add_argument('command')
    cliParser.add_argument('--containerName')
    cliParser.add_argument('--username')

    args = cliParser.parse_args()

    if args.command == 'getUserData':
        getUserData(args)
    elif args.command == 'getContainerList':
        getContainerList(args)
    elif args.command == 'stopContainer':
        stopContainer(args)
    elif args.command == 'restartContainer':
        restartContainer(args)
    elif args.command == 'changeContainerImage':
        changeContainerImage(args)
    else:
        print('This command is not supported')
    sys.exit()