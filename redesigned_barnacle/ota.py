def boot_read(headers, body):
    with open('/boot.py', 'r') as boot:
        return {'status': 200, 'content': boot.read()}


def boot_write(headers, body):
    with open('/card/boot-ota.py', 'w') as boot:
        written = boot.write(body)
        return {'status': 200, 'content': 'wrote {} bytes'.format(written)}
