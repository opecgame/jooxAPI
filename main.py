from urllib.parse import quote
import hashlib, requests

class JOOX:
    """
    bruh who tf wakes up and thinks that it’s a good idea to put 'secret' in plain text.
    """
    
    def request(_): return requests.get(_).json()
    def getSecret(trackId): return hashlib.md5((""+"SaNo0k@t3Nc3nT"+"country=th&lang=en&lyric=1&fs=1&id={}".format(quote(trackId))).encode("UTF-8")).hexdigest()

    def getTrack(trackId): return JOOX.request("https://api-music.sanook.com/openjoox2/v1/track/{}?country=th&lang=en&lyric=1&fs=1&secret={}".format(trackId,JOOX.getSecret(trackId)))
    def getTrending(): return JOOX.request("https://jooxweb-api.tencent.co.th/openapi/footer/all?region=th-th")
    def getQuery(keyword): return JOOX.request("https://api-jooxtt.sanook.com/openjoox/v3/search?country=th&lang=th&keyword={}".format(keyword))
    def getAlbum(albumId): return JOOX.request("https://api-jooxtt.sanook.com/page/albumDetail?id={}&lang=th&country=th&device=desktop".format(albumId))
    
if __name__ == "__main__":
    print(
        JOOX.getTrack("FX05hvgrJ9N3VOX6n3ZFlA=="), # track-info
        JOOX.getTrending(), # recommended albums
        JOOX.getQuery("tuayp") # search
        JOOX.getAlbum("OcAQEWktgfUNGWXJep1fkw==") # album-info
    )
