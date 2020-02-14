import sys

def boot_read(headers, body):
    with open('/boot.py', 'r') as boot:
        return {'status': 200, 'content': boot.read()}


def boot_write(headers, body):
    with open('/card/boot-ota.py', 'w') as boot:
        written = boot.write(body)
        return {'status': 200, 'content': 'wrote {} bytes'.format(written)}

def chain_load(boot_name, paths):
        for p in paths:
                if not p in sys.path:
                        sys.path.append(p)

        return __import__(boot_name)