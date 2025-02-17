import pytest
from io import StringIO
import sys
from src.indented_logger import IndentedLogger

def test_basic_logging(capsys):
    logger = IndentedLogger()
    logger.log("Test message")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Test message"

def test_indentation(capsys):
    logger = IndentedLogger()
    logger.indent()
    result = logger.log("Indented message")
    captured = capsys.readouterr()
    assert result == "  Indented message"
    assert captured.out.strip() == "  Indented message"

def test_multiple_indents(capsys):
    logger = IndentedLogger()
    logger.indent(4)
    result = logger.log("Deeply indented")
    captured = capsys.readouterr()
    assert result == "    Deeply indented"
    assert captured.out.strip() == "    Deeply indented"

def test_base_indent(capsys):
    logger = IndentedLogger(base_indent=2)
    result = logger.log("Base indented")
    captured = capsys.readouterr()
    assert result == "  Base indented"
    assert captured.out.strip() == "  Base indented"

def test_dedent(capsys):
    logger = IndentedLogger()
    logger.indent(4)
    first_result = logger.log("Deeply indented")
    logger.dedent(2)
    second_result = logger.log("Less indented")
    captured = capsys.readouterr()
    assert first_result == "    Deeply indented"
    assert second_result == "  Less indented"

def test_reset_indent(capsys):
    logger = IndentedLogger(base_indent=2)
    logger.indent(4)
    first_result = logger.log("Deeply indented")
    logger.reset_indent()
    second_result = logger.log("Back to base")
    captured = capsys.readouterr()
    assert first_result == "      Deeply indented"
    assert second_result == "  Back to base"

def test_dedent_not_below_base_indent(capsys):
    logger = IndentedLogger(base_indent=2)
    logger.dedent()
    result = logger.log("Should stay at base")
    captured = capsys.readouterr()
    assert result == "  Should stay at base"
    assert captured.out.strip() == "  Should stay at base"

def test_non_string_logging(capsys):
    logger = IndentedLogger()
    logger.indent()
    result = logger.log(42)
    captured = capsys.readouterr()
    assert result == "  42"
    assert captured.out.strip() == "  42"