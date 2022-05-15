from extract_entites import run_recognition
from extract_intent import query_regexes
from convert_to_placeholders import convert_to_placeholders
from extract_custom_entities import extract_customs
import json

def handle_utterance(utterance):
    # extract recognizer entities
    recognizer_results = run_recognition(utterance)

    # extract custom regex entities:
    # custom_entity_results = extract_customs(utterance)

    # combine entities
    # entities = recognizer_results.extend(custom_entity_results)
    entities = []
    for entity in recognizer_results:
        useable_entity = json.dumps(
                        entity,
                        default=lambda o: o.__dict__,
                        indent='\t',
                        ensure_ascii=False)
        useable_entity = json.loads(useable_entity)
        entities.append(useable_entity)


    # breakpoint()

        

  
    # placeholder the utterance using entities and indices
    placeholdered_utterance = convert_to_placeholders(utterance, entities)
    
    # check intent regex for matches
    intents = query_regexes(placeholdered_utterance)

    response = {
        "utterance": utterance,
        "intents": intents,
        "entities": entities
    }
    print(json.dumps(response, indent=4, ensure_ascii=False))
    return response

handle_utterance("order me a pizza in four hours")

