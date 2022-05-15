# Regex NLU
## Goal
- Create a regex nlu intent recognizer with regex entity extraction via [`https://github.com/microsoft/Recognizers-Text`](https://github.com/microsoft/Recognizers-Text)
## How should it look and work?
- Use flask interface on Heroku to allow for 
  - choosing prebuilt entities from the [Recognizers-Text](https://github.com/microsoft/Recognizers-Text] repo
  - adding regex entities
  - writing regex patterns for intents that can refernce these prebuilt entities.
  - testing utterances against the selected entities and intent patterns
  - GET request for running utterances and getting JSON
## What components will it need?
- Flask form interface
- HTTP endpoint for GET requests
- entity extractor module (first)
  - replaces matched entities with placeholder
- intent regex that identifies matched pattern for the placeholdered utterance