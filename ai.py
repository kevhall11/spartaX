# this is going to make the choices using a LLM

import anthropic
import os

ANTHROPIC_API_KEY = os.getenv("claude_key")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

#Options that are viable for the AI 
options = [
        "Option A: Turn right",
        "Option B: turn left",
        "Option C: go foward ",
        "Option D: go backwards",
        "Option E: none of the above"

    ]
def ask_claude_to_decide(criteria):
    """
    Ask Claude to decide between options based on options and criteria.
    
    param options: List of options to choose from.
    param criteria: Criteria to evaluate the options.
    return: Claude's decision and reasoning.
    """
    # Construct the prompt
    prompt = f"""You are a robot that is traveling based off user input. choose the option in which the robot should move
    
    Options:
    {', '.join(options)}

    Criteria for decision-making:
    {criteria}

    Please analyze the options based on the criteria and provide:
    1. the option letter that you choose, just the letter and no other text

    """

    # Send the prompt to Claude
    response = client.messages.create(
        model="claude-3-opus-20240229",  
        max_tokens=500, 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    #return Claude's response
    return response.content[0].text

#seperrates the prompt with a given number and response from claude
def seperate_content(prompt, response):
    
    checker = False
    index1 = 0
    index2 = 0
    ind = 0
    for char in response:
        if(checker):
            if(char == '\n'):
                index2 = ind
                break
        if(char == prompt):
            checker = True
            index1 = ind
        ind = ind + 1

    return response.substring(index1, index2)


##
    def pullOption(str:response):
        ind = response.find("")
