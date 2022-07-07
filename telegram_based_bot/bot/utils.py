from abc import abstractmethod
from pathlib import Path
from random import choice

import yaml
from telegram.message import Message

ASSETS_PATH = Path(__file__).parent.joinpath("../assets")
STICKERS = yaml.safe_load(ASSETS_PATH.joinpath("stickers.yaml").read_text())


class AssetChad:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send(self, message: Message):
        pass


class AssetChadGif(AssetChad):
    def __init__(self, gif: Path):
        self.gif = gif

    def send(self, message: Message):
        message.reply_video(self.gif.read_bytes(), quote=True)


class AssetChadSticker(AssetChad):
    def __init__(self, sticker_file_id: str):
        self.sticker = sticker_file_id

    def send(self, message: Message):
        message.reply_sticker(self.sticker, quote=True)


def get_random_asset_chad() -> AssetChad:
    kind = choice(("gifs", "sticker"))
    if kind == "gifs":
        file = choice(list(ASSETS_PATH.joinpath("gifs").iterdir()))
        return AssetChadGif(file)
    else:
        sticker = choice(STICKERS)
        return AssetChadSticker(sticker)
