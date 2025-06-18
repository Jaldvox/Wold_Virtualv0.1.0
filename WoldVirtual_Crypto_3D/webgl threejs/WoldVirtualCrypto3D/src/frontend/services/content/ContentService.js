import { create } from 'zustand';
import Web3Service from '../blockchain/Web3Service';
import AuthService from '../auth/AuthService';

// Store para el estado del contenido
const useContentStore = create((set) => ({
  assets: {},
  scenes: {},
  addAsset: (asset) => set((state) => ({
    assets: { ...state.assets, [asset.id]: asset }
  })),
  removeAsset: (assetId) => set((state) => {
    const { [assetId]: removed, ...assets } = state.assets;
    return { assets };
  }),
  addScene: (scene) => set((state) => ({
    scenes: { ...state.scenes, [scene.id]: scene }
  })),
  removeScene: (sceneId) => set((state) => {
    const { [sceneId]: removed, ...scenes } = state.scenes;
    return { scenes };
  })
}));

class ContentService {
  constructor() {
    this.store = useContentStore;
    this.web3Service = Web3Service;
    this.authService = AuthService;
  }

  async initialize() {
    try {
      // Cargar assets y escenas iniciales
      await this.loadInitialContent();
      return true;
    } catch (error) {
      console.error('Error inicializando ContentService:', error);
      return false;
    }
  }

  async loadInitialContent() {
    try {
      const response = await fetch(`${process.env.VITE_API_URL}/content/initial`, {
        headers: this.authService.getAuthHeaders()
      });

      if (!response.ok) {
        throw new Error('Error cargando contenido inicial');
      }

      const { assets, scenes } = await response.json();

      // Actualizar store
      assets.forEach(asset => this.store.getState().addAsset(asset));
      scenes.forEach(scene => this.store.getState().addScene(scene));
    } catch (error) {
      console.error('Error cargando contenido inicial:', error);
      throw error;
    }
  }

  async uploadAsset(file, metadata) {
    try {
      // Subir archivo a IPFS
      const ipfsHash = await this.web3Service.uploadToIPFS(file);

      // Crear NFT del asset
      const nftData = {
        name: metadata.name,
        description: metadata.description,
        image: `ipfs://${ipfsHash}`,
        attributes: metadata.attributes || []
      };

      const nftId = await this.web3Service.mintNFT(nftData);

      // Guardar metadata en el backend
      const response = await fetch(`${process.env.VITE_API_URL}/content/assets`, {
        method: 'POST',
        headers: {
          ...this.authService.getAuthHeaders(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          nftId,
          ipfsHash,
          ...metadata
        })
      });

      if (!response.ok) {
        throw new Error('Error guardando metadata del asset');
      }

      const asset = await response.json();
      this.store.getState().addAsset(asset);

      return asset;
    } catch (error) {
      console.error('Error subiendo asset:', error);
      throw error;
    }
  }

  async createScene(sceneData) {
    try {
      const response = await fetch(`${process.env.VITE_API_URL}/content/scenes`, {
        method: 'POST',
        headers: {
          ...this.authService.getAuthHeaders(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(sceneData)
      });

      if (!response.ok) {
        throw new Error('Error creando escena');
      }

      const scene = await response.json();
      this.store.getState().addScene(scene);

      return scene;
    } catch (error) {
      console.error('Error creando escena:', error);
      throw error;
    }
  }

  async updateScene(sceneId, updates) {
    try {
      const response = await fetch(`${process.env.VITE_API_URL}/content/scenes/${sceneId}`, {
        method: 'PATCH',
        headers: {
          ...this.authService.getAuthHeaders(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(updates)
      });

      if (!response.ok) {
        throw new Error('Error actualizando escena');
      }

      const scene = await response.json();
      this.store.getState().addScene(scene);

      return scene;
    } catch (error) {
      console.error('Error actualizando escena:', error);
      throw error;
    }
  }

  async deleteScene(sceneId) {
    try {
      const response = await fetch(`${process.env.VITE_API_URL}/content/scenes/${sceneId}`, {
        method: 'DELETE',
        headers: this.authService.getAuthHeaders()
      });

      if (!response.ok) {
        throw new Error('Error eliminando escena');
      }

      this.store.getState().removeScene(sceneId);
      return true;
    } catch (error) {
      console.error('Error eliminando escena:', error);
      throw error;
    }
  }

  getAsset(assetId) {
    return this.store.getState().assets[assetId];
  }

  getScene(sceneId) {
    return this.store.getState().scenes[sceneId];
  }

  getAllAssets() {
    return Object.values(this.store.getState().assets);
  }

  getAllScenes() {
    return Object.values(this.store.getState().scenes);
  }
}

export default new ContentService(); 