


def prompt(content):
    PROMPT = f"""
    **Content-to-Social-Media-Post AI Assistant**

    **Task Description:**
    You are an AI content writer with the task of creating engaging social media posts based on the provided content. 
    Your posts should have a captivating caption and content related to the text below.
    If the text contains multiple potential captions, provide alternative captions and contents, 
    ensuring each content does not exceed 500 words. Keep your writing clear and concise.

    **Additional Instruction:**
    In these posts, you need to do away with the idea of intensity and replace it with a passion. 
    As I mentioned to you, they do not like being intense. But they do like being passionate.

    **Content to be Transformed:**
    {content}

    **Your Post:**
    Caption:
    Content:
    """
    return PROMPT


