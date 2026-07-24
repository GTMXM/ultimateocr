
from pathlib import Path
import urllib.request


class DatasetDownloader:

    def __init__(self, dataset_root):
        self.dataset_root = Path(dataset_root)

    def download(self, url, output_file):
        output_file = Path(output_file)

        output_file.parent.mkdir(parents=True, exist_ok=True)

        print(f"Downloading:\n{url}\n")

        urllib.request.urlretrieve(url, output_file)

        print(f"\nSaved to:\n{output_file}")
