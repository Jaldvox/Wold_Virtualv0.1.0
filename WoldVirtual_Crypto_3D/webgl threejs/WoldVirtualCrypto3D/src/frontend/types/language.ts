// Tipos de idiomas soportados
export type Language = 'es' | 'en';

// Estructura de las traducciones
export interface Translations {
  common: {
    loading: string;
    error: string;
    success: string;
    warning: string;
    info: string;
  };
  auth: {
    login: string;
    logout: string;
    connectWallet: string;
    disconnectWallet: string;
    walletConnected: string;
    walletDisconnected: string;
  };
  scene: {
    loading: string;
    error: string;
    success: string;
  };
  player: {
    move: string;
    jump: string;
    interact: string;
  };
  ui: {
    settings: string;
    inventory: string;
    chat: string;
    notifications: string;
  };
  errors: {
    walletConnection: string;
    sceneLoad: string;
    playerMove: string;
    networkError: string;
  };
} 