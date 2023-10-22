from typing import Union
import re

def open_file(filepath: str) -> Union[str, None]:
    """
    Open the dump file and return the content
    
    Parameters
    ----------
    filepath : str
        The path to the dump file

    Returns
    -------
    str
        The content of the dump file
    
    Raises
    ------
    FileNotFoundError
        If the file does not exist
    """
    with open(filepath, 'r') as f:
        content = f.read()
    return content

def remove(file_content: str, word: str) -> str:
    """
    Remove lines starting with `SET``

    Parameters
    ----------
    file_content : str
        The content of the dump file
    word : str
        The word to remove

    Returns
    -------
    str
        The content of the dump file without the lines starting with the word
    """
    return '\n'.join([line for line in file_content.split('\n') if not line.startswith(word)])

def replace(file_content: str, initial_word: str, replacement_word: str) -> str:
    """
    Replace true for ‘t’

    Parameters
    ----------
    file_content : str
        The content of the dump file
    initial_word : str
        The word to replace
    replacement_word : str
        The word to replace with

    Returns
    -------
    str
        The content of the dump file with the word replaced
    """
    return file_content.replace(initial_word, replacement_word)

def replace_table_statements(file_content: str) -> str:
    """
    Convert table statements to SQLite format.

    Parameters
    ----------
    file_content : str
        The content of the dump file

    Returns
    -------
    str
        The content of the dump file with the table statements converted
    """
    pattern = r'TABLE [^,]*\.'
    return re.sub(pattern, 'TABLE ', file_content)

def add(file_content: str, term: str, at_top: bool) -> str:
    """
    Add a term to the dump file.

    Parameters
    ----------
    file_content : str
        The content of the dump file
    term : str
        The term to add
    at_top : bool
        Whether to add the term at the top or at the bottom

    Returns
    -------
    str
        The content of the dump file with the term added
    """
    return f"{term}\n{file_content}" if at_top else f"{file_content}\n{term}"

def convert(filepath: str) -> str:
    """
    Convert the PostgreSQL dump file to SQLite

    Parameters
    ----------
    filepath : str
        The path to the dump file

    Returns
    -------
    str
        The content of the dump file converted to SQLite

    Raises
    ------
    FileNotFoundError
        If the file does not exist
    """
    # 1. Open the dump file
    file = open_file(filepath)

    # 2. Remove lines starting with `SET``
    file = remove(file, 'SET')

    # 3. Remove  lines starting with `SELECT pg_catalog``
    file = remove(file, 'SELECT pg_catalog')

    # 4. Replace true for ‘t’
    file = replace(file, 'true', 't')

    # 5. Replace false for ‘f’
    file = replace(file, 'false', 'f')

    # 6. Convert table statements to SQLite format.
    file = replace_table_statements(file)

    # 7. Add `BEGIN;`` as first line and `END;`` as last line
    file = add(file, 'BEGIN;', True)
    file = add(file, 'END;', False)

    # 8. Return the content of the dump file
    return file
