class BeadName(Exception):
    pass


def greate(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise BeadName(name + ' is inapporpriate name')

print('ops')