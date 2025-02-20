import pytest
from src.anagram_validator import is_anagram

def test_valid_anagrams():
    """Test known valid anagram pairs"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True
    assert is_anagram("python", "typhon") == True

def test_invalid_anagrams():
    """Test pairs that are not anagrams"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False
    assert is_anagram("abc", "cab") == True  # valid anagram
    assert is_anagram("aab", "aba") == True  # valid anagram with repeated letters

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("short", "longer") == False
    assert is_anagram("abc", "abcd") == False

def test_invalid_inputs():
    """Test inputs with non-lowercase letters"""
    with pytest.raises(ValueError, match="Inputs must contain only lowercase letters"):
        is_anagram("Hello", "hello")
    
    with pytest.raises(ValueError, match="Inputs must contain only lowercase letters"):
        is_anagram("hello", "Hello!")

def test_single_character():
    """Test single character anagrams"""
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False