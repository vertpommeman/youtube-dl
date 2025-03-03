# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class TF1IE(InfoExtractor):
    """TF1 uses the wat.tv player."""
    _VALID_URL = r'https?://(?:(?:videos|www|lci)\.tf1|(?:www\.)?(?:tfou|ushuaiatv|histoire|tvbreizh))\.fr/(?:[^/]+/)*(?P<id>[^/?#.]+)'
    _TESTS = [{
        'url': 'http://videos.tf1.fr/auto-moto/citroen-grand-c4-picasso-2013-presentation-officielle-8062060.html',
        'info_dict': {
            'id': '10635995',
            'ext': 'mp4',
            'title': 'Citroën Grand C4 Picasso 2013 : présentation officielle',
            'description': 'Vidéo officielle du nouveau Citroën Grand C4 Picasso, lancé à l\'automne 2013.',
        },
        'params': {
            # Sometimes wat serves the whole file with the --test option
            'skip_download': True,
        },
        'expected_warnings': ['HTTP Error 404'],
    }, {
        'url': 'http://www.tfou.fr/chuggington/videos/le-grand-mysterioso-chuggington-7085291-739.html',
        'info_dict': {
            'id': 'le-grand-mysterioso-chuggington-7085291-739',
            'ext': 'mp4',
            'title': 'Le grand Mystérioso - Chuggington',
            'description': 'Le grand Mystérioso - Emery rêve qu\'un article lui soit consacré dans le journal.',
            'upload_date': '20150103',
        },
        'params': {
            # Sometimes wat serves the whole file with the --test option
            'skip_download': True,
        },
        'skip': 'HTTP Error 410: Gone',
    }, {
        'url': 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html',
        'only_matching': True,
    }, {
        'url': 'http://lci.tf1.fr/sept-a-huit/videos/sept-a-huit-du-24-mai-2015-8611550.html',
        'only_matching': True,
    }, {
        'url': 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html',
        'only_matching': True,
    }, {
        'url': 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html',
        'info_dict': {
            'id': '13641379',
            'ext': 'mp4',
            'title': 'Quotidien, première partie du 11 juin 2019',
            'description': 'Retrouvez l’intégralité du replay de la première partie de Quotidien du 11 juin. On parle des enfants français rapatriés de Syrie avec Salhia Brakhlia, de la décision du New York Times d’arrêter les dessins politiques avec Lilia Hassaine, on part voir les Bleues à J-1 de leur rencontre avec la ...',
            'upload_date': '20190611',
        },
        'params': {
            # Sometimes wat serves the whole file with the --test option
            'skip_download': True,
        },
    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        wat_id = self._html_search_regex(
            r'"streamId":"(?P<id>\d{8})"',
            webpage, 'wat id', group='id')
        return self.url_result('wat:%s' % wat_id, 'Wat')
