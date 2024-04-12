import datasets
import json

from dataloader import load_corpus_file

RESOURCE_CONFIGURATION = json.load("sb_config.json")

__URL = RESOURCE_CONFIGURATION["url"]
__DESCRIPTION = RESOURCE_CONFIGURATION["description"]
__CITATION = RESOURCE_CONFIGURATION["citation"]
__HOMEPAGE = RESOURCE_CONFIGURATION["homepage"]
__RESOURCE_NAME = RESOURCE_CONFIGURATION["resource_name"]

class Config(datasets.BuilderConfig):
    """BuilderConfig for Config."""

    def __init__(self, **kwargs):
        f"""Dataset from a corpus.
        **kwargs: keyword arguments forwarded to super.
        """
        super(Config, self).__init__(**kwargs)


class Builder(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIG_CLASS = Config
    BUILDER_CONFIGS = []

    def _info(self):
        f = datasets.Features({
            "sentence": datasets.Value("string")
        })
        return datasets.DatasetInfo(
            features=f,
            supervised_keys=None,
            description=__DESCRIPTION,
            homepage=__HOMEPAGE,
            citation=__CITATION
        )

    def _split_generators(self, dl_manager):
        #load_corpus_file(__URL)
        #dl_manager.download_and_extract(__URL)
        raise NotImplementedError        

    def _generate_examples(self):
        for i, line in load_corpus_file(__URL):
            yield i, {"text" : line.rstrip()}