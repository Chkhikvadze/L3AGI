from typing import Optional
from pydantic import BaseModel
from enums import ChatMessageVersion

class ChatMessageInput(BaseModel):
    prompt: str
    version: ChatMessageVersion
    is_private_chat: bool
    local_chat_message_ref_id: Optional[str] = None
    parent_id: Optional[str] = None


class NegotiateOutput(BaseModel):
    url: str
