import hashlib

def shorten_url(url: str) -> str:
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()[:6]


if __name__ == "__main__":
    long_url = input("URL kiriting: ")
    short = shorten_url(long_url)
    print(f"Short URL: https://short.ly/{short}")
