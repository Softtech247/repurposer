
OPENAI_API_KEY = "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"

def prompt(content):
    PROMPT = f"""
    **Content-to-Social-Media-Post AI Assistant**

    **Task Description:**
    You are an AI content writer with the task of creating engaging social media posts based on the provided content. Your posts should have a captivating caption and content related to the text below. If the text contains multiple potential captions, provide alternative captions and contents, ensuring each content does not exceed 500 words. Keep your writing clear and concise.

    **Content to be Transformed:**
    {content}

    **Your Post:**
    Caption:
    Content:
    """
    return PROMPT



PROMPT = """
    Your output must use the following Template:
     Highlights
    + Bulletpoint

    You are smart agent, your role is to read the content giving below and bring out at least 3 quotes or message highlights in the content 
    in the bulletpoint form. You Must write more than four words quotes for each highlights. Do not include thank you or appreciation.
      Strictly Message and Highlights. Do not put your text inside quotation marks.  
    The text should be as simple as possible and it should have enough meaning to be Christian Social Media Post. 
    
    Here is the content :
    
    {content_here}
    """


def prompt_highlight(content):
     PROMPT = f"""
    Your output must use the following Template:

    #### Highlights
    + Bulletpoint

    You are smart agent, your role is to read the content giving below and bring out at least 3 quotes or message highlights in the content
    The text should be as simple as possible. here is the content : {content}
    """
     return  PROMPT

PROMPT = """
    Your output must use the following Template:
     Highlights
    + Bulletpoint

    You are smart agent, your role is to read the content giving below and bring out at least 3 quotes or message highlights in the content 
    in the bulletpoint form. You Must write more than four words quotes for each highlights. Do not include thank you or appreciation.
      Strictly Message and Highlights. Do not put your text inside quotation marks.  
    The text should be as simple as possible and it should have enough meaning to be Christian Social Media Post. 
    
    Here is the content :
    
    {content_here}
    """