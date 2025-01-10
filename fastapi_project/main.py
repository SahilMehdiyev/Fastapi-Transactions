from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .crud import get_transaction, create_transaction, get_all_transactions
from .schemas import TransactionCreate, Transaction
from .models import Base
from .database import engine

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/transactions/", response_model=Transaction)
async def create_new_transaction(transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    db_transaction = Transaction(**transaction.dict())
    return await create_transaction(db, db_transaction)

@app.get("/transactions/{transaction_id}", response_model=Transaction)
async def read_transaction(transaction_id: int, db: AsyncSession = Depends(get_db)):
    transaction = await get_transaction(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.get("/transactions/", response_model=list[Transaction])
async def list_transactions(db: AsyncSession = Depends(get_db)):
    return await get_all_transactions(db)
