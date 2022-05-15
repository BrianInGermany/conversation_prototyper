# This script is passed an utterance and an entity JSON
# it uses the json to placeholder remaining entities.
# it outputs a JSON including a placeholdered utterance and the original utterance
# it passes its output to the intent_regex module


from html import entities
from numpy import append

from sklearn.decomposition import non_negative_factorization


def convert_to_placeholders(utterance, entity_obj):
    # iterate over all entities, filter out those contained within others.
    
    nonnested_entities = []
    for entity in entity_obj:
        for entity2 in entity_obj:
            if utterance[entity["start"]:entity["end"]] in utterance[entity2["start"]:entity2["end"]]:
                entity_obj.remove(entity)
        # breakpoint()
        nonnested_entities = entity_obj
    placeholder_utterance = utterance
    for nonnested in nonnested_entities:
        placeholder_utterance = placeholder_utterance[:nonnested["start"]] + "@" + nonnested["type_name"] + placeholder_utterance[nonnested["end"] + 1:] 
    # breakpoint()
    print("placeholdered: " + placeholder_utterance)
    return placeholder_utterance



# {
#         "start": 16,
#         "end": 28,
#         "resolution": {
#                 "values": [
#                         {
#                                 "timex": "2022-05-15T19:57:19",
#                                 "type": "datetime",
#                                 "value": "2022-05-15 19:57:19"
#                         }
#                 ]
#         },
#         "text": "in 10 minutes",
#         "type_name": "datetimeV2.datetime"
# }


    return placeholdered_utt  