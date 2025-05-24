from ai_engine import lang_processor, test_case_generator
from test_runners.python_runner import pytest_runner

def run_pipeline():
    with open("test_interface/nl_input/sample_test.txt") as f:
        text = f.read()
    lang = lang_processor.detect_language(text)
    english_text = lang_processor.translate_to_english(text, lang)
    gherkin = test_case_generator.generate_gherkin(english_text)
    print("Generated Gherkin:\n", gherkin)
    pytest_runner.run_tests()

if __name__ == "__main__":
    run_pipeline()