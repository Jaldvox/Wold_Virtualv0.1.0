// Tipos para Web3Service
export interface Web3Service {
  initialize(): Promise<boolean>;
  provider: any;
  contracts: {
    nft: any;
    token: any;
  };
  mintNFT(data: NFTData): Promise<string>;
  transferNFT(to: string, tokenId: string): Promise<boolean>;
  getNFTMetadata(tokenId: string): Promise<NFTMetadata>;
  uploadToIPFS(file: File): Promise<string>;
  getBalance(address: string): Promise<string>;
}

export interface NFTData {
  name: string;
  description: string;
  image: string;
  attributes?: Array<{
    trait_type: string;
    value: string | number;
  }>;
}

export interface NFTMetadata {
  id: string;
  name: string;
  description: string;
  image: string;
  attributes: Array<{
    trait_type: string;
    value: string | number;
  }>;
  owner: string;
  createdAt: string;
}

// Tipos para AuthService
export interface AuthService {
  initialize(): Promise<boolean>;
  loginWithWallet(): Promise<{ user: User; token: string }>;
  validateToken(token: string): Promise<boolean>;
  refreshToken(): Promise<boolean>;
  logout(): void;
  getUser(): User | null;
  getToken(): string | null;
  isAuthenticated(): boolean;
  getAuthHeaders(): Record<string, string>;
}

export interface User {
  id: string;
  address: string;
  username?: string;
  avatar?: string;
  createdAt: string;
  updatedAt: string;
}

// Tipos para SyncService
export interface SyncService {
  initialize(): Promise<boolean>;
  updateUserPosition(userId: string, position: [number, number, number]): void;
  updateUserRotation(userId: string, rotation: [number, number, number]): void;
  updateObjectPosition(objectId: string, position: [number, number, number]): void;
  updateObjectRotation(objectId: string, rotation: [number, number, number]): void;
  createObject(object: SceneObject): void;
  removeObject(objectId: string): void;
  getConnectedUsers(): Record<string, User>;
  getObjects(): Record<string, SceneObject>;
  isConnected(): boolean;
  cleanup(): void;
}

export interface SceneObject {
  id: string;
  type: 'model' | 'light' | 'camera' | 'group';
  position: [number, number, number];
  rotation: [number, number, number];
  scale: [number, number, number];
  data: any;
  owner: string;
  createdAt: string;
  updatedAt: string;
}

// Tipos para ContentService
export interface ContentService {
  initialize(): Promise<boolean>;
  uploadAsset(file: File, metadata: AssetMetadata): Promise<Asset>;
  createScene(sceneData: SceneData): Promise<Scene>;
  updateScene(sceneId: string, updates: Partial<SceneData>): Promise<Scene>;
  deleteScene(sceneId: string): Promise<boolean>;
  getAsset(assetId: string): Asset | undefined;
  getScene(sceneId: string): Scene | undefined;
  getAllAssets(): Asset[];
  getAllScenes(): Scene[];
}

export interface AssetMetadata {
  name: string;
  description: string;
  type: 'model' | 'texture' | 'audio' | 'video';
  format: string;
  attributes?: Record<string, any>;
}

export interface Asset {
  id: string;
  nftId: string;
  ipfsHash: string;
  metadata: AssetMetadata;
  owner: string;
  createdAt: string;
  updatedAt: string;
}

export interface SceneData {
  name: string;
  description: string;
  objects: SceneObject[];
  settings: {
    environment: string;
    lighting: {
      ambient: [number, number, number];
      directional: [number, number, number];
    };
    physics: {
      gravity: number;
      friction: number;
    };
  };
  owner: string;
  isPublic: boolean;
}

export interface Scene {
  id: string;
  data: SceneData;
  createdAt: string;
  updatedAt: string;
} 