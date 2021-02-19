"""
This type stub file was generated by pyright.
"""
from pathlib import Path
from typing import (Any, Iterable, Iterator, List, Optional, Sequence, Tuple,
                    TypeVar)

from spacy.tokens import Span

_data_path = Path(__file__).parent / "data"
_PRINT_ENV = False

class registry(object):
    languages = ...
    architectures = ...
    lookups = ...
    factories = ...
    displacy_colors = ...

def set_env_log(value): ...
def lang_class_is_loaded(lang):
    """Check whether a Language class is already loaded. Language classes are
    loaded lazily, to avoid expensive setup code associated with the language
    data.

    lang (unicode): Two-letter language code, e.g. 'en'.
    RETURNS (bool): Whether a Language class has been loaded.
    """
    ...

def get_lang_class(lang):
    """Import and load a Language class.

    lang (unicode): Two-letter language code, e.g. 'en'.
    RETURNS (Language): Language class.
    """
    ...

def set_lang_class(name, cls):
    """Set a custom Language class name that can be loaded via get_lang_class.

    name (unicode): Name of Language class.
    cls (Language): Language class.
    """
    ...

def get_data_path(require_exists: bool = ...):
    """Get path to spaCy data directory.

    require_exists (bool): Only return path if it exists, otherwise None.
    RETURNS (Path or None): Data path or None.
    """
    ...

def set_data_path(path):
    """Set path to spaCy data directory.

    path (unicode or Path): Path to new data directory.
    """
    ...

def make_layer(arch_config): ...
def ensure_path(path):
    """Ensure string is converted to a Path.

    path: Anything. If string, it's converted to Path.
    RETURNS: Path or original argument.
    """
    ...

def load_language_data(path):
    """Load JSON language data using the given path as a base. If the provided
    path isn't present, will attempt to load a gzipped version before giving up.

    path (unicode / Path): The data to load.
    RETURNS: The loaded data.
    """
    ...

def get_module_path(module): ...
def load_model(name, **overrides):
    """Load a model from a shortcut link, package or data path.

    name (unicode): Package name, shortcut link or model path.
    **overrides: Specific overrides, like pipeline components to disable.
    RETURNS (Language): `Language` class with the loaded model.
    """
    ...

def load_model_from_link(name, **overrides):
    """Load a model from a shortcut link, or directory in spaCy data path."""
    ...

def load_model_from_package(name, **overrides):
    """Load a model from an installed package."""
    ...

def load_model_from_path(model_path, meta: bool = ..., **overrides):
    """Load a model from a data directory path. Creates Language class with
    pipeline from meta.json and then calls from_disk() with path."""
    ...

def load_model_from_init_py(init_file, **overrides):
    """Helper function to use in the `load()` method of a model package's
    __init__.py.

    init_file (unicode): Path to model's __init__.py, i.e. `__file__`.
    **overrides: Specific overrides, like pipeline components to disable.
    RETURNS (Language): `Language` class with loaded model.
    """
    ...

def get_model_meta(path):
    """Get model meta.json from a directory path and validate its contents.

    path (unicode or Path): Path to model directory.
    RETURNS (dict): The model's meta data.
    """
    ...

def is_package(name):
    """Check if string maps to a package installed via pip.

    name (unicode): Name of package.
    RETURNS (bool): True if installed package, False if not.
    """
    ...

def get_package_path(name):
    """Get the path to an installed package.

    name (unicode): Package name.
    RETURNS (Path): Path to installed package.
    """
    ...

def is_in_jupyter():
    """Check if user is running spaCy from a Jupyter notebook by detecting the
    IPython kernel. Mainly used for the displaCy visualizer.
    RETURNS (bool): True if in Jupyter, False if not.
    """
    ...

def get_component_name(component): ...
def get_cuda_stream(require: bool = ..., non_blocking: bool = ...): ...
def get_async(stream, numpy_array): ...
def env_opt(name, default: Optional[Any] = ...): ...
def read_regex(path): ...
def compile_prefix_regex(entries):
    """Compile a sequence of prefix rules into a regex object.

    entries (tuple): The prefix rules, e.g. spacy.lang.punctuation.TOKENIZER_PREFIXES.
    RETURNS (regex object): The regex object. to be used for Tokenizer.prefix_search.
    """
    ...

def compile_suffix_regex(entries):
    """Compile a sequence of suffix rules into a regex object.

    entries (tuple): The suffix rules, e.g. spacy.lang.punctuation.TOKENIZER_SUFFIXES.
    RETURNS (regex object): The regex object. to be used for Tokenizer.suffix_search.
    """
    ...

def compile_infix_regex(entries):
    """Compile a sequence of infix rules into a regex object.

    entries (tuple): The infix rules, e.g. spacy.lang.punctuation.TOKENIZER_INFIXES.
    RETURNS (regex object): The regex object. to be used for Tokenizer.infix_finditer.
    """
    ...

def add_lookups(default_func, *lookups):
    """Extend an attribute function with special cases. If a word is in the
    lookups, the value is returned. Otherwise the previous function is used.

    default_func (callable): The default function to execute.
    *lookups (dict): Lookup dictionary mapping string to attribute value.
    RETURNS (callable): Lexical attribute getter.
    """
    ...

def _get_attr_unless_lookup(default_func, lookups, string): ...
def update_exc(base_exceptions, *addition_dicts):
    """Update and validate tokenizer exceptions. Will overwrite exceptions.

    base_exceptions (dict): Base exceptions.
    *addition_dicts (dict): Exceptions to add to the base dict, in order.
    RETURNS (dict): Combined tokenizer exceptions.
    """
    ...

def expand_exc(excs, search, replace):
    """Find string in tokenizer exceptions, duplicate entry and replace string.
    For example, to add additional versions with typographic apostrophes.

    excs (dict): Tokenizer exceptions.
    search (unicode): String to find and replace.
    replace (unicode): Replacement.
    RETURNS (dict): Combined tokenizer exceptions.
    """
    ...

def normalize_slice(length, start, stop, step: Optional[Any] = ...): ...

T = TypeVar("T")

def minibatch(items: Iterable[T], size=...) -> Iterator[List[T]]: ...
def compounding(start, stop, compound):
    """Yield an infinite series of compounding values. Each time the
    generator is called, a value is produced by multiplying the previous
    value by the compound rate.

    EXAMPLE:
      >>> sizes = compounding(1., 10., 1.5)
      >>> assert next(sizes) == 1.
      >>> assert next(sizes) == 1 * 1.5
      >>> assert next(sizes) == 1.5 * 1.5
    """
    ...

def stepping(start, stop, steps):
    """Yield an infinite series of values that step from a start value to a
    final value over some number of steps. Each step is (stop-start)/steps.

    After the final value is reached, the generator continues yielding that
    value.

    EXAMPLE:
      >>> sizes = stepping(1., 200., 100)
      >>> assert next(sizes) == 1.
      >>> assert next(sizes) == 1 * (200.-1.) / 100
      >>> assert next(sizes) == 1 + (200.-1.) / 100 + (200.-1.) / 100
    """
    ...

def decaying(start, stop, decay):
    """Yield an infinite series of linearly decaying values."""
    ...

def minibatch_by_words(items, size, tuples: bool = ..., count_words=...):
    """Create minibatches of a given number of words."""
    ...

def itershuffle(iterable, bufsize=...):
    """Shuffle an iterator. This works by holding `bufsize` items back
    and yielding them sometime later. Obviously, this is not unbiased –
    but should be good enough for batching. Larger bufsize means less bias.
    From https://gist.github.com/andres-erbsen/1307752

    iterable (iterable): Iterator to shuffle.
    bufsize (int): Items to hold back.
    YIELDS (iterable): The shuffled iterator.
    """
    ...

def filter_spans(spans: Iterable[Span]) -> List[Span]: ...
def to_bytes(getters, exclude): ...
def from_bytes(bytes_data, setters, exclude): ...
def to_disk(path, writers, exclude): ...
def from_disk(path, readers, exclude): ...
def minify_html(html):
    """Perform a template-specific, rudimentary HTML minification for displaCy.
    Disclaimer: NOT a general-purpose solution, only removes indentation and
    newlines.

    html (unicode): Markup to minify.
    RETURNS (unicode): "Minified" HTML.
    """
    ...

def escape_html(text):
    """Replace <, >, &, " with their HTML encoded representation. Intended to
    prevent HTML errors in rendered displaCy markup.

    text (unicode): The original text.
    RETURNS (unicode): Equivalent text to be safely used within HTML.
    """
    ...

def use_gpu(gpu_id): ...
def fix_random_seed(seed=...): ...
def get_json_validator(schema): ...
def validate_schema(schema):
    """Validate a given schema. This just checks if the schema itself is valid."""
    ...

def validate_json(data, validator):
    """Validate data against a given JSON schema (see https://json-schema.org).

    data: JSON-serializable data to validate.
    validator (jsonschema.DraftXValidator): The validator.
    RETURNS (list): A list of error messages, if available.
    """
    ...

def get_serialization_exclude(serializers, exclude, kwargs):
    """Helper function to validate serialization args and manage transition from
    keyword arguments (pre v2.1) to exclude argument.
    """
    ...

class SimpleFrozenDict(dict):
    """Simplified implementation of a frozen dict, mainly used as default
    function or method argument (for arguments that should default to empty
    dictionary). Will raise an error if user or spaCy attempts to add to dict.
    """

    def __setitem__(self, key, value): ...
    def pop(self, key, default: Optional[Any] = ...): ...
    def update(self, other): ...

class DummyTokenizer(object):
    def to_bytes(self, **kwargs): ...
    def from_bytes(self, _bytes_data, **kwargs): ...
    def to_disk(self, _path, **kwargs): ...
    def from_disk(self, _path, **kwargs): ...
