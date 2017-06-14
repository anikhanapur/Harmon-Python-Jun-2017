import ConfigParser


def create_config(path):

    config = ConfigParser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Ariel")
    config.set("Settings", "font-size", "18pts")

    with open(path, 'w') as config_file:
        config.write(config_file)
        print('done')


if __name__ == '__main__':
    create_config('app-config.ini')


