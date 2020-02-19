"""
This type stub file was generated by pyright.
"""

def iob2json(input_data, n_sents=..., no_print: bool = ..., *args, **kwargs):
    """
    Convert IOB files with one sentence per line and tags separated with '|'
    into JSON format for use with train cli. IOB and IOB2 are accepted.

    Sample formats:

    I|O like|O London|I-GPE and|O New|B-GPE York|I-GPE City|I-GPE .|O
    I|O like|O London|B-GPE and|O New|B-GPE York|I-GPE City|I-GPE .|O
    I|PRP|O like|VBP|O London|NNP|I-GPE and|CC|O New|NNP|B-GPE York|NNP|I-GPE City|NNP|I-GPE .|.|O
    I|PRP|O like|VBP|O London|NNP|B-GPE and|CC|O New|NNP|B-GPE York|NNP|I-GPE City|NNP|I-GPE .|.|O
    """
    ...

def read_iob(raw_sents): ...
def merge_sentences(docs, n_sents): ...
