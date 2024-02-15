import cdb
import anagrams
import time


class TestCDB:
    def test_adjectives(self):
        adjectives = list(cdb.get_adjectives('cdb-sample.xml'))
        print(adjectives)
        assert len(adjectives) == 131
        assert set(adjectives) == {'ongelijk', 'rot', 'publiek', 'kapot',
                'romantisch', 'zindelijk', 'stekelig', 'plastisch',
                'onhoudbaar', 'traag', 'gevestigd', 'broos', 'verdraaid',
                'automatisch', 'berekend', 'gewijd', 'rekkelijk', 'onfeilbaar',
                'finaal', 'redelijk', 'raak', 'proper', 'verzadigd',
                'onbekwaam', 'wrang', 'progressief', 'onbeperkt', 'ijzig',
                'alleenstaand', 'afkerig', 'nodig', 'zuiver', 'ongewoon',
                'fenomenaal', 'best', 'glashelder', 'praktisch', 'rijk', 'zat',
                'vruchtbaar', 'stroef', 'elektrisch', 'beschikbaar',
                'makkelijk', 'temporeel', 'solidair', 'intiem', 'vrij',
                'onnatuurlijk', 'bezet', 'disponibel', 'verplicht', 'werelds',
                'goed', 'verdacht', 'onbedekt', 'pittig', 'kokend',
                'speculatief', 'week', 'gesloten', 'vergevensgezind',
                'opgemaakt', 'onontwikkeld', 'gewoon', 'tweeslachtig', 'beter',
                'ongemakkelijk', 'geraffineerd', 'slijmerig', 'lekker',
                'nietig', 'ver', 'flauw', 'respectabel', 'gering',
                'plaatselijk', 'dol', 'gedekt', 'scheef', 'statisch',
                'heilzaam', 'handig', 'bezeten', 'vervallen', 'links',
                'ellendig', 'rein', 'aanstaande', 'genadig', 'abnormaal',
                'gaar', 'solide', 'driftig', 'onzijdig', 'onwaarschijnlijk',
                'historisch', 'onbuigbaar', 'simpel', 'verward', 'vet',
                'ecologisch', 'naar', 'algemeen', 'hysterisch', 'rechteloos',
                'gekleurd', 'vlezig', 'glazig', 'krampachtig', 'ontrouw',
                'down', 'overjarig', 'uit', 'heerlijk', 'bijzonder',
                'vleselijk', 'onvruchtbaar', 'klein', 'ongebonden', 'beroerd',
                'onbeschaafd', 'verbonden', 'polair', 'steriel', 'lam',
                'gezwollen', 'onaanzienlijk', 'lokaal', 'link', 'centraal'}


class TestAnagrams:
    def test_find(self):
        assert anagrams.find('eten', 'words.json') == {'eten', 'teen', 'neet'}

    def test_find_many(self):
        start = time.perf_counter()
        anagrams.find_many('query.txt', 'words.json')
        end = time.perf_counter()
        assert ((end - start) < 1)
