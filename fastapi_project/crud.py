from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Transaction

async def get_transaction(db: AsyncSession, transaction_id: int):
    result = await db.execute(select(Transaction).filter(Transaction.id == transaction_id))
    return result.scalars().first()

async def create_transaction(db: AsyncSession, transaction: Transaction):
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)
    return transaction

async def get_all_transactions(db: AsyncSession):
    result = await db.execute(select(Transaction))
    return result.scalars().all()
