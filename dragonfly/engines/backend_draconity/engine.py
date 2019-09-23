from ..base        import EngineBase


class DraconityEngine(EngineBase):
    """ Draconity-based engine backend. """

    _name = "draconity"

    def __init__(self):
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
