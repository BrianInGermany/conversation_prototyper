# this script is passed the entity JSON an utterance, and a placeholdered utterance
# it outputs the matched intents in matching order, the entity json, and the original utterance.
import yaml
import re

def query_regexes(placeholdered_utterance):
    with open("components/nlu_model.yaml", "r", encoding="utf-8") as nlu_model:
        # load intent Regexes
        model_data = yaml.load(nlu_model)
        intents = model_data["intents"]
        matching_intents = []
        for intent in intents:
            for pattern in intents[intent]:
                
                match = re.match(pattern, placeholdered_utterance, re.IGNORECASE)
                if match:
                    matching_intents.append(intent)
                    break

        return matching_intents

 
    