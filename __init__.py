from pbf.utils import Utils, MetaData
from pbf.setup import logger

try:
    import tensorflow
    import numpy
    import skimage
except ImportError:
    logger.debug("asdasd")
    Utils.installPackage("tensorflow")
    Utils.installPackage("numpy")
    Utils.installPackage("scikit-image")
    Utils.installPackage("typing_extensions --upgrade")

from . import classify_nsfw


meta_data = MetaData(
    name="Nsfw",
    version="0.0.1",
    versionCode=1,
    description="Block Not Suitable For Work Content",
    author="XzyStudio",
    license="MIT",
    keywords=["pbf", "plugin", "nsfw"],
    readme="""
# Nsfw
使用Yahoo开源的Nsfw制作，可以检测不宜图片

## 使用
pbf.pluginsManager.require('nsfw').check(file_path)
返回一个NSFW值，表示当前图片的不宜程度
    """
)

class Api:
    @staticmethod
    def check(file_path: str):
        return classify_nsfw.main(file_path)['nsfw']

