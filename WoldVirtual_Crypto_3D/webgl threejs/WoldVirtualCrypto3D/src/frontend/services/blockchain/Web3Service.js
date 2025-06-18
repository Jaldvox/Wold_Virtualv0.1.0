import Web3 from 'web3';
import { ethers } from 'ethers';
import { create } from 'ipfs-http-client';

class Web3Service {
  constructor() {
    this.web3 = null;
    this.provider = null;
    this.ipfs = null;
    this.contracts = {};
    this.initialized = false;
  }

  async initialize() {
    try {
      // Inicializar Web3
      if (window.ethereum) {
        this.provider = new ethers.providers.Web3Provider(window.ethereum);
        this.web3 = new Web3(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
      } else {
        throw new Error('Por favor instala MetaMask para usar esta aplicación');
      }

      // Inicializar IPFS
      this.ipfs = create({
        host: 'ipfs.infura.io',
        port: 5001,
        protocol: 'https'
      });

      // Cargar contratos
      await this.loadContracts();

      this.initialized = true;
      return true;
    } catch (error) {
      console.error('Error inicializando Web3Service:', error);
      return false;
    }
  }

  async loadContracts() {
    try {
      // Cargar ABI de contratos
      const nftContractABI = await import('@/contracts/NFTContract.json');
      const tokenContractABI = await import('@/contracts/TokenContract.json');

      // Inicializar contratos
      this.contracts.nft = new this.web3.eth.Contract(
        nftContractABI.default,
        process.env.VITE_NFT_CONTRACT_ADDRESS
      );

      this.contracts.token = new this.web3.eth.Contract(
        tokenContractABI.default,
        process.env.VITE_TOKEN_CONTRACT_ADDRESS
      );
    } catch (error) {
      console.error('Error cargando contratos:', error);
    }
  }

  async mintNFT(metadata) {
    try {
      if (!this.initialized) throw new Error('Web3Service no inicializado');

      // Subir metadata a IPFS
      const ipfsResult = await this.ipfs.add(JSON.stringify(metadata));
      const tokenURI = `ipfs://${ipfsResult.path}`;

      // Obtener cuenta actual
      const accounts = await this.web3.eth.getAccounts();
      const account = accounts[0];

      // Mintear NFT
      const result = await this.contracts.nft.methods
        .mint(account, tokenURI)
        .send({ from: account });

      return result;
    } catch (error) {
      console.error('Error minting NFT:', error);
      throw error;
    }
  }

  async transferNFT(to, tokenId) {
    try {
      if (!this.initialized) throw new Error('Web3Service no inicializado');

      const accounts = await this.web3.eth.getAccounts();
      const account = accounts[0];

      const result = await this.contracts.nft.methods
        .transferFrom(account, to, tokenId)
        .send({ from: account });

      return result;
    } catch (error) {
      console.error('Error transferring NFT:', error);
      throw error;
    }
  }

  async getNFTMetadata(tokenId) {
    try {
      if (!this.initialized) throw new Error('Web3Service no inicializado');

      const tokenURI = await this.contracts.nft.methods.tokenURI(tokenId).call();
      const metadata = await this.ipfs.cat(tokenURI.replace('ipfs://', ''));
      return JSON.parse(metadata);
    } catch (error) {
      console.error('Error getting NFT metadata:', error);
      throw error;
    }
  }

  async uploadToIPFS(file) {
    try {
      if (!this.initialized) throw new Error('Web3Service no inicializado');

      const result = await this.ipfs.add(file);
      return `ipfs://${result.path}`;
    } catch (error) {
      console.error('Error uploading to IPFS:', error);
      throw error;
    }
  }

  async getBalance(address) {
    try {
      if (!this.initialized) throw new Error('Web3Service no inicializado');

      const balance = await this.web3.eth.getBalance(address);
      return this.web3.utils.fromWei(balance, 'ether');
    } catch (error) {
      console.error('Error getting balance:', error);
      throw error;
    }
  }
}

export default new Web3Service(); 