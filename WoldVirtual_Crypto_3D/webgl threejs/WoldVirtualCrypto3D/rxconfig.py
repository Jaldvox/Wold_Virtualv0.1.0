import reflex as rx
import os
from dotenv import load_dotenv

load_dotenv()

config = rx.Config(
    app_name="metaverse_crypto_3d",
    db_url=os.getenv("DATABASE_URL", "sqlite:///metaverse.db"),
    env=rx.Env.DEV,
    frontend_port=3000,
    backend_port=8000,
    api_url="http://localhost:8000",
    cors_allowed_origins=["http://localhost:3000", "http://localhost:5173"],
    blockchain_provider=os.getenv("BLOCKCHAIN_PROVIDER", "http://localhost:8545"),
    ipfs_gateway=os.getenv("IPFS_GATEWAY", "https://ipfs.io/ipfs/"),
    web3_provider=os.getenv("WEB3_PROVIDER", "http://localhost:8545")
)