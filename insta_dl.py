import argparse

parser = argparse.ArgumentParser(description='Download images from an Instagram post')
parser.add_argument("instagram_url", help="URL to the Instagram post")
parser.add_argument("destination", help="Path where you want to save the images")

if __name__ == "__main__":
    args = parser.parse_args()
