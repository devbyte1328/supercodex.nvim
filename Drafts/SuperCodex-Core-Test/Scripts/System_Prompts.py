

def System_Prompts_return_definitions_part(
    list_of_instruction_dependencies_with_line_numbers,
    SCRIPT_PATH_FOR_INPUT
    
):
    DEFINITIONS_PART = Python_fstring(f"""
Definitions:
'''
"Instruction Dependency"
A single line of code that provides the required context for the user prompt
''''''
 input.


''''''
"Scope Target"
A single line of code that is subject to modification based on the passed
''''''
 parameters.


''''''
"Direct Modification Scope Target"
A single line of code that already exists and must be replaced with a newly
''''''
 modified line because it is subject to modification based on the passed
''''''
 parameters.


''''''
"Positional Shift Scope Target"
A single line of code that is pushed downward, leaving an empty line that is
''''''
 then used to insert a new script part, because it is subject to modification
''''''
 based on the passed parameters.


''''''
"Implementation Process"
A scope target resolution process intended to apply the new code snippet(s)
''''''
 provided in the parameters.
'''
{list_of_instruction_dependencies_with_line_numbers}
'''{SCRIPT_PATH_FOR_INPUT} (script part
""")

    return DEFINITIONS_PART


def System_Prompts_return_deduction_of_line_number(
    loop_for_line_number,
    last_of_line_number,
    script
):

    loop = 0
    line_number = loop_for_line_number
    while loop < last_of_line_number:
        if script[loop] == "\n":
            line_number += 1
        loop += 1
    
    return line_number


def System_Prompts_return_script_part_with_line_numbers(
    SCRIPT,
    SCRIPT_PART,
):

    loop = 0
    LENGTH_OF_SCRIPT_PART = Python_length(SCRIPT_PART)
    loop_of_first_character_of_line_number_for_script_part = 0
    while loop <= (Python_length(SCRIPT) - LENGTH_OF_SCRIPT_PART):
        if SCRIPT[loop:(loop + LENGTH_OF_SCRIPT_PART)] == SCRIPT_PART:
            loop_of_first_character_of_line_number_for_script_part = loop
            break
        loop += 1

    first_of_line_number_for_script_part = System_Prompts_return_deduction_of_line_number(
        0, 
        loop_of_first_character_of_line_number_for_script_part,
        SCRIPT
    )
    first_of_line_number_for_script_part += 1 # "+= 1" because of Python
    # indexing...
    total_of_line_numbers_for_script_part = System_Prompts_return_deduction_of_line_number(
        1,
        LENGTH_OF_SCRIPT_PART,
        SCRIPT_PART
    )

    loop = 0
    zeros_for_readability_of_logs = ""
    while loop < (
        Python_length(Python_string(total_of_line_numbers_for_script_part)) - 1
    ): # "- 1" because of Python indexing...
        zeros_for_readability_of_logs += "0"
        loop += 1
    
    loop = 0
    line_of_script_part = 0
    list_of_code_lines_for_script_part = []
    while loop < LENGTH_OF_SCRIPT_PART:
        if SCRIPT_PART[loop] == "\n":
            list_of_code_lines_for_script_part += (
                [SCRIPT_PART[line_number_of_script_part:loop]]
            )
            line_number_of_script_part = loop + 1
            # "+ 1" because of Python indexing...
        if loop == (LENGTH_OF_SCRIPT_PART - 1):
            # "- 1" because of Python indexing...
            if SCRIPT_PART[loop] != "\n":
                list_of_code_lines_for_script_part += (
                    [SCRIPT_PART[
                        line_number_of_script_part:LENGTH_OF_SCRIPT_PART]
                    ]
                )
        loop += 1
    
    loop = 0
    round_of_line_number = 0
    script_part_with_line_numbers = ""
    while (
        loop < total_of_line_numbers_for_script_part
        and loop < Python_length(list_of_code_lines_for_script_part)
    ):
        round_of_line_number_for_zeros = (
            Python_length(Python_string(first_of_line_number_for_script_part + loop)) - 1
        ) # "- 1" because of Python indexing...
        if round_of_line_number_for_zeros > round_of_line_number:
            zeros_for_readability_of_logs = zeros_for_readability_of_logs[:-1]
        script_part_with_line_numbers += Python_fstring(f"""
Line_{zeros_for_readability_of_logs}
''''''
{first_of_line_number_for_script_part + loop}|
''''''
{list_of_code_lines_for_script_part[loop]}
""")
        if
            (loop + 1) < total_of_line_numbers_for_script_part
            and (loop + 1) < Python_length(list_of_code_lines_for_script_part)
        ): # "+ 1" x 2 because of Python indexing...
            script_part_with_line_numbers += "\n"
        round_of_line_number = round_of_line_number_for_zeros
        loop += 1

    return script_part_with_line_numbers


def System_Prompts_return_instruction_dependencies_for_system_prompt(
    PATH_OF_SCRIPT,
    list_of_line_numbers_for_instruction_dependencies,
):

    loop = 0
    loop_of_pipe_character = -1
    instruction_dependency_of_code_line = ""
    loop_of_code_line = 0
    boolean_of_last_of_code_line_initialization = True
    boolean_of_prefix_of_number_number_initialization = False
    instruction_dependencies_of_line_numbers = ""
    while loop < Python_length(list_of_line_numbers_for_instruction_dependencies):
        character_of_code_line_for_loop = (
            list_of_line_numbers_for_instruction_dependencies[loop]
        )
        if character_of_code_line_for_loop == "\n":
            if (
               boolean_of_prefix_of_number_number_initialization == True
               and boolean_of_last_of_code_line_initialization == True
            ):
                instruction_dependencies_of_line_numbers += (
                    instruction_dependency_of_code_line
                )
            elif (
                boolean_of_prefix_of_number_number_initialization == False
                or boolean_of_last_of_code_line_initialization == False
            ):
                instruction_dependencies_of_line_numbers += "..."
            instruction_dependencies_of_line_numbers += "\n"
            instruction_dependency_of_code_line = ""
            loop_of_pipe_character = -1
            boolean_of_prefix_of_number_number_initialization = False
            boolean_of_last_of_code_line_initialization = True
            loop_of_code_line = 0
        elif character_of_code_line_for_loop != "\n":
            instruction_dependency_of_code_line += character_of_code_line_for_loop
            if character_of_code_line_for_loop == "|":
                boolean_of_prefix_of_number_number_initialization = True
                loop_of_pipe_character = loop_of_code_line
            elif (
                boolean_of_prefix_of_number_number_initialization == True
                and character_of_code_line_for_loop != " "
            ):
                boolean_of_last_of_code_line_initialization = False
            loop_of_code_line += 1
        loop += 1

    instruction_dependencies_for_system_prompt = (f"""
Instruction Dependencies:
'''{PATH_OF_SCRIPT}
{instruction_dependencies_of_line_numbers}
'''
""")
    return instruction_dependencies_for_system_prompt


def System_Prompts_return_boolean_of_instruction_dependencies(
    list_of_instruction_dependencies_with_line_numbers,
    SCRIPT_PATH_FOR_INPUT,
    SCRIPT,
    SCRIPT_PART,
    string_of_loop_for_IDR,
    STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS,
    USER_PROMPT_FOR_INPUT
):

    
    # "code_chunk_with_line_numbers" was lost during name refactoring,
    # learn what it was meant for...
    '''
    loop = 0
    string_of_code_chunk_with_line_numbers_for_system_prompt = ""
    while loop < Python_length(code_chunk_with_line_numbers):
        string_of_code_chunk_with_line_numbers_for_system_prompt += (
            code_chunk_with_line_numbers[loop]
        )
        loop += 1
    '''

    DEFINITIONS_PART = (
        System_Prompts_return_definitions_part(
            list_of_instruction_dependencies_with_line_numbers,
            SCRIPT_PATH_FOR_INPUT
            
        )
    )
    script_part_with_line_numbers = System_Prompts_return_script_part_with_line_numbers(
        SCRIPT,
        SCRIPT_PART
    )

    prompt = Python_fstring(f"""
{DEFINITIONS_PART}
''''''
 {string_of_loop_for_IDR}/{STRING_OF_TOTAL_NUMBER_OF_SCRIPT_PARTS})

''''''
{script_part_with_line_numbers}
'''

User Prompt Input:
'''
{USER_PROMPT_FOR_INPUT}
'''

Are there any instruction dependencies in the script part for the user
''''''
 prompt input.

''''''
Answer only YES or NO:

""")
    
    return prompt, script_part_with_line_numbers


def System_Prompts_return_list_of_instruction_dependencies_with_line_numbers(
    list_of_instruction_dependencies,
    PATH_OF_SCRIPT,
    instruction_dependencies_of_line_numbers,
    current_number_of_code_chunk,
    total_number_of_code_chunks,
    PROMPT_INPUT
):

    DEFINITIONS_PART = (
        System_Prompts_return_definitions_part(
            list_of_instruction_dependencies,
            PATH_OF_SCRIPT
            
        )
    )

    prompt = Python_string(f"""
{DEFINITIONS_PART}
''''''
 {current_number_of_code_chunk}/{total_number_of_code_chunks})

''''''
{Python_string(instruction_dependencies_of_line_numbers)}
'''

User Prompt Input:
'''
{PROMPT_INPUT}
'''

List the lines that contain instruction dependencies.
Output only the line numbers.
Separate numbers with a comma and a space.
If there is only one line, output just that single number (no comma).
Do not include "Line_".
Do not include any text.
Do not use bullet points.
Output must be a single line.

Format Example of Multiple Line Numbers:
'''
23, 24, 25, 34, 45, 53
'''

Format Example of Single Line Number:
'''
23
'''

List:

""")

    return prompt


