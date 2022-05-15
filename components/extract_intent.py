# this script is passed the entity JSON an utterance, and a placeholdered utterance
# it outputs the matched intents in matching order, the entity json, and the original utterance.
import yaml

def query_regexes(placeholdered_utterance):
    with open("components/nlu_model.yaml", "r", encoding="utf-8") as nlu_model:
        # load intent Regexes
        pass
    pass