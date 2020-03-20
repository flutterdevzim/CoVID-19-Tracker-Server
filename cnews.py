from newsapi import NewsApiClient
api =
print(api.get_everything(q='corona'))

class CoronaNews(object):

    def __init__(self, api_key="841f303d46ae476a814ffddb8977c818"):
        # load data
        self.api = NewsApiClient(api_key="841f303d46ae476a814ffddb8977c818")
        # may cause problems later as data is fetched everytime class is instantiated
        # Solution: Cache Data on server or in Mobile App (sqlife)
        self.data = self.api.get_everything(q=q)

    @property
    def articles(self) -> list:
        return self.data['articles']
