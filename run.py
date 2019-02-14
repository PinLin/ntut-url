import os
from ntut_url import app


def main():
    SERVER_PORT = int(os.environ.get('SERVER_PORT') or 5000)

    app.run(port=SERVER_PORT, threaded=True)


if __name__ == '__main__':
    main()
