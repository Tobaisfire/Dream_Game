
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from typing_extensions import Annotated, TypedDict
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool
from config import lang_smith_api, hugging_face
class network:

    def __init__(self):
        pass


    def llm_selection(llm_id: str,max_new_tokens=512,penalty=1.03):

        """
        llm_id  : huggingface_repo_id
        """

        llm = HuggingFaceEndpoint(
        repo_id=llm_id,
    
            max_new_tokens=512,
            do_sample=False,
            repetition_penalty=penalty,
            huggingfacehub_api_token=hugging_face,

        )
      

        return llm
    
       







@tool
def test() -> str:
    """gives out owner name"""
    return "Owner name is keval"
# class add(TypedDict):
#     """Add two integers."""

#     # Annotations must have the type and can optionally include a default value and description (in that order).
#     a: Annotated[int, ..., "First integer"]
#     b: Annotated[int, ..., "Second integer"]




