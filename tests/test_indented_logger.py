import io
import sys
import pytest
from src.indented_logger import IndentedLogger

def test_basic_logging(capsys):
    logger = IndentedLogger()
    logger.log("Test message")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Test message"

def test_indentation(capsys):
    logger = IndentedLogger()
    logger.indent()
    logger.log("Indented message")
    captured = capsys.readouterr()
    assert captured.out.strip() == "  Indented message"

def test_multiple_indents(capsys):
    logger = IndentedLogger()
    logger.indent(4)
    logger.log("Deeply indented")
    captured = capsys.readouterr()
    assert captured.out.strip() == "    Deeply indented"

def test_base_indent(capsys):
    logger = IndentedLogger(base_indent=2)
    logger.log("Base indented")
    captured = capsys.readouterr()
    assert captured.out.strip() == "  Base indented"

def test_dedent(capsys):
    # Redirect stdout to a StringIO object
    logger = IndentedLogger()
    logger.indent(4)
    logger.log("Deeply indented")
    logger.dedent(2)
    logger.log("Less indented")
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    assert lines[0] == "    Deeply indented"
    assert lines[1] == "  Less indented"

def test_reset_indent(capsys):
    logger = IndentedLogger(base_indent=2)
    logger.indent(4)
    logger.log("Deeply indented")
    logger.reset_indent()
    logger.log("Back to base")
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    assert lines[0] == "      Deeply indented"
    assert lines[1] == "  Back to base"

def test_dedent_not_below_base_indent(capsys):
    logger = IndentedLogger(base_indent=2)
    logger.dedent()
    logger.log("Should stay at base")
    captured = capsys.readouterr()
    assert captured.out.strip() == "  Should stay at base"

def test_non_string_logging(capsys):
    logger = IndentedLogger()
    logger.indent()
    logger.log(42)
    captured = capsys.readouterr()
    assert captured.out.strip() == "  42"