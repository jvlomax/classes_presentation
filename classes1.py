import sys
class ConfigParser:

    def parse(self, file):
        self.file.read()


if __name__ == "__main__":
    parser = ConfigParser()
    with open(sys.argv[1]) as fp:
        parser.parse(fp)
