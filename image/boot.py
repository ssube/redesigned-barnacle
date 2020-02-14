import machine
import os
import sys


def boot_main():
    # load config
    card = machine.SDCard()
    os.mount(card, '/card')
    sys.path.append('/card/lib')

    from redesigned_barnacle.config import load_config
    from redesigned_barnacle.ota import chain_load

    config = load_config('/card', 'config.yml')
    print('Card config: ', config)

    # chain the card loader
    chain_module = chain_load(config['image_name'], [
        '/card/lib',
        '/card/app',
    ])

    return chain_module.chain_main(config)


if __name__ == "__main__":
    boot_main()
