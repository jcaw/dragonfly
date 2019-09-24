import os
import platform

import toml

from ..base        import EngineBase


class ConfigError(IOError):
    """Error to be raised when the config could not be loaded."""


def _config_path():
    """
    Get the Draconity config file's path on this platform.

    Just returns the path - the config file itself isn't guaranteed to exist
    yet.

    :returns: path to where the config would be stored
    :rtype: str

    """
    path_tail = ".talon/draconity.toml"
    if platform.system() == "Darwin":  # Mac
        # TODO: What if there's no HOME? Draonity has a backup method we need to emulate.
        path_root = os.path.expandvars("$HOME")
    elif platform.system() == "Windows":
        path_root = os.path.expandvars("%APPDATA%")
    else:
        return None
    return os.path.join(path_root, path_tail)


def _extract_simple_config(raw_config):
    """
    Extract a flat config dict from Draconity's raw config.

    Only extracts information relevant to the connection.

    If the raw config does not contain all necessary components, a ConfigError
    will be raised.

    :raw_config: raw config dict from directly decoding the toml.
    :type raw_config: dict
    :returns: a dictionary with 3 keys, "secret", "host" and "port".
    :rtype: dict

    """
    simple_config = {}
    try:
        simple_config["secret"] = raw_config["secret"]
    except IndexError:
        raise ConfigError("No secret configured in draconity config.")
    try:
        simple_config["host"] = raw_config["socket"][0]["host"]
    except IndexError:
        raise ConfigError("No host configured in draconity config.")
    try:
        simple_config["port"] = raw_config["socket"][0]["port"]
    except IndexError:
        raise ConfigError("No port configured in draconity config.")
    return simple_config


def _load_config():
    """
    Load the draconity config from disk.

    If the config is incomplete, a `ConfigError` will be raised.

    :returns: a dictionary with 3 keys, "secret", "host" and "port".
    :rtype: dict

    """
    config_path = _config_path()
    if not config_path:
        raise OSError("Draconity not supported on this platform.")
    raw_config = toml.load(config_path)
    return _extract_simple_config(raw_config)


class DraconityEngine(EngineBase):
    """ Draconity-based engine backend. """

    _name = "draconity"

    def __init__(self):
        self._config = _load_config()
        super(DraconityEngine, self).__init__()

    def connect(self):
        raise NotImplementedError("Not yet implemented.")

    def disconnect(self):
        raise NotImplementedError("Not yet implemented.")

    def _build_grammar_wrapper(self):
        raise NotImplementedError("Not yet implemented.")

    def _load_grammar(self, grammar):
        raise NotImplementedError("Not yet implemented.")

    def _unload_grammar(self, grammar):
        raise NotImplementedError("Not yet implemented.")

    def update_list(self, lst, grammar):
        raise NotImplementedError("Not yet implemented.")

    def activate_grammar(self, grammar):
        raise NotImplementedError("Not yet implemented.")

    def deactivate_grammar(self, grammar):
        raise NotImplementedError("Not yet implemented.")

    def activate_rule(self, rule, grammar):
        raise NotImplementedError("Not yet implemented.")

    def deactivate_rule(self, rule, grammar):
        raise NotImplementedError("Not yet implemented.")

    def set_exclusiveness(self, grammar, exclusive):
        raise NotImplementedError("Not yet implemented.")

    def mimic(self, words):
        """ Mimic a recognition of the given *words*. """
        raise NotImplementedError("Not yet implemented.")

    def speak(self, text):
        """ Speak the given *text* using text-to-speech. """
        raise NotImplementedError("Not yet implemented.")

    # def _get_language(self):
    #     raise NotImplementedError("Engine %s not implemented." % self)
