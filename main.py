import sys
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}
MIDPASS_URL = "https://info.midpass.ru/api/request"


def main():
    argv = sys.argv

    if len(argv) < 2:
        print("Provide order id")
        print("Example use: python main.py 123456789")
        return

    data = get_data(argv[1])
    print_status(data)


def get_data(order_id):
    r = requests.get(f"{MIDPASS_URL}/{order_id}", headers=headers)
    data = r.json()
    return data


def print_status(data):
    passport_status = data["passportStatus"]["name"]
    internal_status = data["internalStatus"]["name"]
    percentage = data["internalStatus"]["percent"]
    print("Internal Status: ", internal_status)
    print("Passport Status: ", passport_status)
    print(f"Readines: {percentage}%")


if __name__ == "__main__":
    main()
