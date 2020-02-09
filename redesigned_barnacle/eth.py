from redesigned_barnacle.compat import LAN


def eth_check(eth):
    online = eth.connected
    network = eth.ifconfig()

    print('Online: {}'.format(online))
    if not online:
        return False

    print('Network: {}'.format(network))
    if network[0] == '0.0.0.0':
        return False

    return True


def eth_connected(eth):
    try:
        return eth.connected
    except:
        return eth.isconnected()


def eth_start(config, mdc, mdio, phy_type, clock_mode, phy_addr, power_pin=None):
    if power_pin != None:
        power_pin.value(1)

    eth = LAN(
        mdc=mdc,
        mdio=mdio,
        phy_addr=phy_addr,
        phy_type=phy_type,
        clock_mode=clock_mode
    )

    if 'net_ip' in config:
        net_config = (
            config['net_ip'], config['net_mask'],
            config['net_gw'], config['net_dns']
        )
        print('Connecting with config: {}'.format(net_config))
        eth.ifconfig(net_config)
    else:
        print('Connecting with DHCP')

    eth.active(True)
    return eth
