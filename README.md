# File Format and Structure Documentation

> Documentation generated with ChatGPT and edited by Lastek 

___
- [x] See `prompts.txt` for how to generate cards with an LLM.
- [x] Check cs430 example files for how it should look and to expect.
___

This document explains the file formats and structures required for the Anki card processing program. Follow these guidelines to correctly format input and tag files, and interpret the output.

Input Files
## Cards File (`<filename>.txt`)

‼️ Must have `.txt` extension ‼️

Purpose: Contains the question-answer pairs to be processed.

Format:
 ```
Card #:
Q: [Question] for the question.
A: [Answer] for the answer.
```

__Multi-line answers should be indented or separated by new lines.__

Example:  
```
Card #:
Q: What is the difference between logical schema and physical schema?  
A:
    Logical schema: The overall logical structure of the database (e.g., information about customers and accounts in a bank).  
    Physical schema: The overall physical structure of the database (how data is stored on disk).  
```
            
## Tags File (`<filename>_tags.txt`)

Purpose: Maps keywords in answers to corresponding tags.

Format:

- A Python dictionary structure where:

    - Keys are keywords (case-insensitive).

    - Values are corresponding tags.

Example:
```python
{
    "database": "database",
    "DBMS": "DBMS",
    "transaction": "transactions",
    "schema": "schema",
    "query": "query_processing"
}
```

## Output File
Processed Cards File (`<filename>_anki.txt`)

Purpose: Contains the formatted cards ready for Anki import.

Format:

- Each line represents one card, consisting of three tab-separated fields:


| Question | Answer | Tags |
| ----------- | ----------- | ----------- | 
Question | Answer (multi-line content replaced with <br> tags). | Tags (space-separated). |

Example:
```
What is a database?   A database is a large, integrated collection of data that models a real-world enterprise, including entities (e.g., students, courses) and relationships (e.g., Lady Gaga is taking CS 430).   database
```

## How the Program Works

Input:

- The program reads `<filename>.txt` for card data.

- It reads `<filename>_tags.txt` for keyword-to-tag mapping.

Processing:

- Replaces multi-line answers with `<br>` for Anki compatibility.

- Matches keywords in answers to generate corresponding tags.

Output:

- Writes the formatted cards with tags to `<filename>_anki.txt`.

## Usage Instructions

1. Prepare your input files:

2. Create `<filename>.txt` with question-answer pairs.

3. Create `<filename>_tags.txt` with the keyword-to-tag dictionary.@

4. Run the program:

   - Ensure the script and files are in the same directory.

    - Ensure the script in a Python environment.

5. Import into Anki:

    - Go into your deck and select File > Import.
    - Import the generated file and verify everything looks ok.

## Notes

- Modify tags.txt to adapt tags to your specific needs.

- Ensure the input files follow the required structure for accurate processing.

