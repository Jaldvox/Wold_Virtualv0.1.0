from fastapi import APIRouter, HTTPException
from src.backend.blockchain.web3_client import Web3Client
from src.backend.state.BlockchainState import BlockchainState

router = APIRouter()
blockchain_state = BlockchainState()

@router.post("/blockchain/transaction")
async def create_transaction(transaction_data: dict):
    try:
        transaction_hash = await Web3Client.send_transaction(transaction_data)
        blockchain_state.add_transaction(transaction_hash)
        return {"status": "success", "transaction_hash": transaction_hash}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/blockchain/transactions")
async def get_transactions():
    return blockchain_state.get_all_transactions()

@router.get("/blockchain/status")
async def get_blockchain_status():
    status = await Web3Client.get_status()
    return {"status": status}