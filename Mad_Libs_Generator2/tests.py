import pytest
from main_code import generate_story

def test_story_generation_with_input():
    # Test the generate_story function with specific arguments
    result = generate_story('happy', 'blue', 'playful', 'cat', 'jumped', 'quickly', 'soft', 'pillow')
    expected_output = "------------------------------------------\n"\
                      "The happy blue fox jumped over the playful cat.\n"\
                      "It jumped quickly and looked very soft.\n"\
                      "The quick, brown cat landed on a pillow.\n"\
                      "------------------------------------------\n"
    assert result == expected_output

def test_story_generation_without_input(monkeypatch):
    # Test the generate_story function without providing input
    # Simulate user input using monkeypatch
    monkeypatch.setattr('builtins.input', lambda _: 'happy blue playful cat jumped quickly soft pillow')
    
    result = generate_story()
    expected_output = "------------------------------------------\n"\
                      "The happy blue fox jumped over the playful cat.\n"\
                      "It jumped quickly and looked very soft.\n"\
                      "The quick, brown cat landed on a pillow.\n"\
                      "------------------------------------------\n"
    assert result == expected_output
