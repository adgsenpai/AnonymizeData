from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import re


def anonymize(text_to_anonymize):
    analyzer = AnalyzerEngine()
    analyzer_results = analyzer.analyze(text=text_to_anonymize, entities=[
                                        "PHONE_NUMBER", "PERSON", "LOCATION", "ID", "TITLE", "EMAIL_ADDRESS"], language="en")
    anonymizer = AnonymizerEngine()
    anonymized_results = anonymizer.anonymize(
        text=text_to_anonymize,
        analyzer_results=analyzer_results,
        operators={"DEFAULT": OperatorConfig("replace", {"new_value": "<ANONYMIZED>"}),
                   "PHONE_NUMBER": OperatorConfig("mask", {"type": "mask", "masking_char": "*", "chars_to_mask": 12, "from_end": True}),
                   "PERSON": OperatorConfig("mask", {"type": "mask", "masking_char": "*", "chars_to_mask": 12, "from_end": True}),
                   "LOCATION": OperatorConfig("mask", {"type": "mask", "masking_char": "*", "chars_to_mask": 12, "from_end": True}),
                   "ID": OperatorConfig("mask", {"type": "mask", "masking_char": "*", "chars_to_mask": 12, "from_end": True}),
                   "TITLE": OperatorConfig("mask", {"type": "mask", "masking_char": "*", "chars_to_mask": 12, "from_end": True}),
                   "EMAIL_ADDRESS": OperatorConfig("mask", {"type": "mask", "masking_char": "*", "chars_to_mask": 12, "from_end": True}),
                   },


    )
    output = anonymized_results.text

    output = re.sub(r'/^[0-9]{13}$/', '*****', output)
    return output


if __name__ == "__main__":
    print(anonymize("My name is John Doe and my phone number is 1234567890"))
