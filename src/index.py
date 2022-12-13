from app import Application
from console_io import ConsoleIO


def main():
    app = Application(ConsoleIO())
    app.start()


if __name__ == "__main__":
    main()
