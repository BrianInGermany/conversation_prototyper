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
        entity_is_nested = False
        for entity2 in entity_obj:
            if (entity["start"] >= entity2["start"] and entity["end"] <= entity2["end"]):
                # (entity is nested)
                entity_is_nested = True
                break
        if entity_is_nested == False:
            nonnested_entities.append(entity)
    
    for nonnested in nonnested_entities:
        utterance = utterance[:nonnested["start"]] + nonnested["typename"] + utterance[nonnested["end"]:] 

    return utterance



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