from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey, DECIMAL, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)
    receiver_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)
    amount = Column(DECIMAL(20, 2), nullable=True)
    transaction_unique_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=True)
    meta_data = Column(JSON, nullable=True)
    note = Column(Text, nullable=True)
    deletion_reason = Column(Text, nullable=True)
    transaction_number = Column(String(150), nullable=False)
    transaction_type = Column(String(50), nullable=True)
    device_id = Column(String(50), nullable=True)
    status = Column(String(20), default="created")
    cancel_reason = Column(String(300), nullable=True)
    fail_reason = Column(Text, nullable=True)
    is_refund = Column(Boolean, default=False)
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    sender = relationship("Account", foreign_keys=[sender_id])
    receiver = relationship("Account", foreign_keys=[receiver_id])
    created_by = relationship("User", foreign_keys=[created_by_id])
