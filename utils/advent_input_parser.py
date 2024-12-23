# File: advent_input_parser.py

import json
from typing import List, Any, Tuple

def parse_integers(input_str: str) -> List[int]:
    """
    Parse a multiline string into a list of integers.
    """
    return [int(line) for line in input_str.strip().splitlines()]

def parse_strings(input_str: str) -> List[str]:
    """
    Parse a multiline string into a list of strings.
    """
    return input_str.strip().splitlines()

def parse_grid(input_str: str, as_int: bool = False) -> List[List[Any]]:
    """
    Parse a multiline string into a 2D grid.
    """
    grid = [list(line) for line in input_str.strip().splitlines()]
    return [[int(cell) for cell in row] if as_int else row for row in grid]

def parse_csv(input_str: str, delimiter: str = ",") -> List[List[str]]:
    """
    Parse a CSV formatted string into a list of lists.
    """
    return [line.split(delimiter) for line in input_str.strip().splitlines()]

def parse_json(input_str: str) -> Any:
    """
    Parse a JSON string into a Python object.
    """
    return json.loads(input_str)

def split_by_empty_lines(input_str: str) -> List[str]:
    """
    Split input into groups separated by empty lines.
    """
    return input_str.strip().split("\n\n")

def parse_coordinates(input_str: str) -> List[Tuple[int, int]]:
    """
    Parse coordinates from lines of 'x,y' format.
    """
    return [tuple(map(int, line.split(','))) for line in input_str.strip().splitlines()]

def parse_two_lists(input_str: str) -> Tuple[List[int], List[int]]:
    """
    Parse input where each line contains two numbers, one for each list.
    
    Args:
        input_str (str): Multiline string where each line contains two numbers separated by whitespace.
        
    Returns:
        Tuple[List[int], List[int]]: Two lists, one with the first numbers and one with the second numbers.
    """
    list1, list2 = [], []
    for line in input_str.strip().splitlines():
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    return list1, list2
