from pydantic import BaseModel, UUID4
from typing import Optional, Any
from datetime import datetime

class TransactionBase(BaseModel):
    sender_id: Optional[int]
    receiver_id: Optional[int]
    amount: Optional[float]
    transaction_type: Optional[str]
    device_id: Optional[str]
    status: Optional[str] = "created"
    meta_data: Optional[Any]
    note: Optional[str]
    deletion_reason: Optional[str]
    cancel_reason: Optional[str]
    fail_reason: Optional[str]
    is_refund: Optional[bool] = False

class TransactionCreate(TransactionBase):
    transaction_number: str

class Transaction(TransactionBase):
    id: int
    transaction_unique_id: Optional[UUID4]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
