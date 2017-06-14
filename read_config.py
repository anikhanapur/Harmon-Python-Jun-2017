import ConfigParser

def readConfig(path):

    config = ConfigParser.ConfigParser()
    config.read(path)

    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font-size")

    print(font, font_size)


if __name__ == '__main__':
	readConfig('app-config.ini')
