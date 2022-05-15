import json
from typing import List
import recognizers_suite as Recognizers
from recognizers_suite import Culture, ModelResult

# Use English for the Recognizers culture
DEFAULT_CULTURE = Culture.English

# Read from Console and recognize
def run_recognition(user_input):
   
    results = parse_all(user_input, DEFAULT_CULTURE)
    # Flatten results
    results = [item for sublist in results for item in sublist]

    # Write results on console
    print()
    print(f'I found the following entities ({len(results)}):'
            if results else 'I found no entities.')
    print()

    for result in results:
        print(
            json.dumps(
                result,
                default=lambda o: o.__dict__,
                indent='\t',
                ensure_ascii=False))
        print()
    return results


def parse_all(user_input: str, culture: str) -> List[List[ModelResult]]:
    return [
        # Number recognizer - This function will find any number from the input
        # E.g "I have two apples" will return "2".
        Recognizers.recognize_number(user_input, culture),

        # Ordinal number recognizer - This function will find any ordinal number
        # E.g "eleventh" will return "11".
        Recognizers.recognize_ordinal(user_input, culture),

        # Percentage recognizer - This function will find any number presented as percentage
        # E.g "one hundred percents" will return "100%"
        Recognizers.recognize_percentage(user_input, culture),

        # Age recognizer - This function will find any age number presented
        # E.g "After ninety five years of age, perspectives change" will return
        # "95 Year"
        Recognizers.recognize_age(user_input, culture),

        # Currency recognizer - This function will find any currency presented
        # E.g "Interest expense in the 1988 third quarter was $ 75.3 million"
        # will return "75300000 Dollar"
        Recognizers.recognize_currency(user_input, culture),

        # Dimension recognizer - This function will find any dimension presented E.g "The six-mile trip to my airport
        # hotel that had taken 20 minutes earlier in the day took more than
        # three hours." will return "6 Mile"
        Recognizers.recognize_dimension(user_input, culture),

        # Temperature recognizer - This function will find any temperature presented
        # E.g "Set the temperature to 30 degrees celsius" will return "30 C"
        Recognizers.recognize_temperature(user_input, culture),

        # DateTime recognizer - This function will find any Date even if its write in colloquial language -
        # E.g "I'll go back 8pm today" will return "2017-10-04 20:00:00"
        Recognizers.recognize_datetime(user_input, culture),

        # PhoneNumber recognizer will find any phone number presented
        # E.g "My phone number is ( 19 ) 38294427."
        Recognizers.recognize_phone_number(user_input, culture),

        # Email recognizer will find any phone number presented
        # E.g "Please write to me at Dave@abc.com for more information on task
        # #A1"
        Recognizers.recognize_email(user_input, culture),
    ]
