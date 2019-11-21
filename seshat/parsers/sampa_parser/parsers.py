from abc import ABCMeta
from collections import OrderedDict, defaultdict

from seshat.parsers.base import BaseCustomParser, AnnotationError
from voxpopuli import Voice


class BaseSampaParser(BaseCustomParser, metaclass=ABCMeta):
    """A parser that checks if a phoneme """
    NAME = "Sampa Parser (%s)"  # this name should be unique, and will be displayed in Seshat's interface
    LANGUAGE = None

    def __init__(self):
        phonemizer = Voice(lang="en")
        pho_len = defaultdict(set)
        for pho in phonemizer.phonemes._all:
            pho_len[len(pho)].add(pho)
        # ordering dict by descending length
        self.pho_len = OrderedDict(
            sorted(pho_len.items(), key=lambda x: x[0], reverse=True))

    @classmethod
    def get_name(cls):
        return cls.NAME % cls.LANGUAGE

    def check_annotation(self, annot: str) -> None:
        """Parses the phonemes in a string to a list of phoneme, raises
        an error if it fails """
        original_str = str(annot)
        pho_str = str(annot)
        pho_list = []
        while pho_str:
            parsed_phoneme = False
            # trying to match longest phoneme names first
            for len_pho, pho_set in self.pho_len.items():
                if pho_str[:len_pho] in pho_set:
                    pho_list.append(pho_str[:len_pho])
                    pho_str = pho_str[len_pho:]
                    parsed_phoneme = True
                    break
            if not parsed_phoneme:
                raise AnnotationError("Can't parse phonetic form %s (stuck at %s)"
                                      % (original_str, pho_str))


class FrenchSampaParser(BaseSampaParser):
    LANGUAGE = "fr"


class SpanishSampaParser(BaseSampaParser):
    LANGUAGE = "es"


class EnglishSampaParser(BaseSampaParser):
    LANGUAGE = "en"