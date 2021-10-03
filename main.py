from urllib.parse import quote
import hashlib

class Pilgrim:
    getTrack = lambda trackId : "https://api-music.sanook.com/openjoox2/v1/track/{}?country=th&lang=en&lyric=1&fs=1&secret={}".format(trackId, Pilgrim.getSecret(trackId))
    todayAlbum = "https://jooxweb-api.tencent.co.th/openapi/footer/all?region=th-th"

    def getSecret(trackId):
        secretKey = "SaNo0k@t3Nc3nT"
        quoteBuilder = "country=th&lang=en&lyric=1&fs=1&id={}".format(quote(trackId)) # too lazy to use lambda, map, keys. lol
        return hashlib.md5((""+secretKey+quoteBuilder).encode("UTF-8")).hexdigest()

if __name__ == "__main__":
    print(Pilgrim.getTrack("FX05hvgrJ9N3VOX6n3ZFlA==")) # https://api-music.sanook.com/openjoox2/v1/track/FX05hvgrJ9N3VOX6n3ZFlA==?country=th&lang=en&lyric=1&fs=1&secret=33da9f3c81f56ec3df689badd402d85b
