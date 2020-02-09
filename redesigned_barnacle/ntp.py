from redesigned_barnacle.compat import ticks_diff, ticks_ms

import socket
import struct
import time

def ntp_header_unpack(line):
    return (
        (line & 0xC0000000) >> 30,
        (line & 0x38000000) >> 27,
        (line & 0x07000000) >> 24,
        (line & 0x00FF0000) >> 16,
        (line & 0x0000FF00) >> 8,
        (line & 0x000000FF),
    )


def ntp_fetch():
    buffer = 1024
    epoch = 2208988800
    host = 'pool.ntp.org'
    port = 123

    request_addr = socket.getaddrinfo(host, port)
    request_data = '\x1b' + 47 * '\0'
    time_start = ticks_ms()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(request_data.encode(), request_addr[0][4])
    response_data, response_addr = sock.recvfrom(buffer)
    sock.close()

    time_stop = ticks_ms()
    time_diff = ticks_diff(time_stop, time_start)

    ntp_packet = struct.unpack('!12I', response_data)
    ntp_header = ntp_header_unpack(ntp_packet[0])
    ntp_second = ntp_packet[10] - epoch

    print('got {} from {}, {} seconds since epoch with {} ms RTT'.format(
        ntp_header,
        response_addr,
        ntp_second,
        time_diff,
    ))

    if ntp_header[0] == 3:
        raise Exception('server clock is not synchronized')

    if ntp_header[2] != 4:
        raise Exception('time source is not a server (type {})'.format(ntp_header[2]))

    rtt_second = time_diff / 2000
    return time.localtime(ntp_second + rtt_second)


def ntp_format():
    return '{0:4d}-{1:02d}-{2:02d}T{3:02d}:{4:02d}:{5:02d}Z'.format(*ntp_fetch())
