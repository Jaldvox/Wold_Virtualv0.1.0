import { Translations } from '../types/language';

export const translations: Record<string, Translations> = {
  es: {
    common: {
      loading: 'Cargando...',
      error: 'Error',
      success: 'Éxito',
      warning: 'Advertencia',
      info: 'Información',
    },
    auth: {
      login: 'Iniciar sesión',
      logout: 'Cerrar sesión',
      connectWallet: 'Conectar billetera',
      disconnectWallet: 'Desconectar billetera',
      walletConnected: 'Billetera conectada',
      walletDisconnected: 'Billetera desconectada',
    },
    scene: {
      loading: 'Cargando escena...',
      error: 'Error al cargar la escena',
      success: 'Escena cargada correctamente',
    },
    player: {
      move: 'Mover',
      jump: 'Saltar',
      interact: 'Interactuar',
    },
    ui: {
      settings: 'Configuración',
      inventory: 'Inventario',
      chat: 'Chat',
      notifications: 'Notificaciones',
    },
    errors: {
      walletConnection: 'Error al conectar la billetera',
      sceneLoad: 'Error al cargar la escena',
      playerMove: 'Error al mover al jugador',
      networkError: 'Error de red',
    },
  },
  en: {
    common: {
      loading: 'Loading...',
      error: 'Error',
      success: 'Success',
      warning: 'Warning',
      info: 'Information',
    },
    auth: {
      login: 'Login',
      logout: 'Logout',
      connectWallet: 'Connect wallet',
      disconnectWallet: 'Disconnect wallet',
      walletConnected: 'Wallet connected',
      walletDisconnected: 'Wallet disconnected',
    },
    scene: {
      loading: 'Loading scene...',
      error: 'Error loading scene',
      success: 'Scene loaded successfully',
    },
    player: {
      move: 'Move',
      jump: 'Jump',
      interact: 'Interact',
    },
    ui: {
      settings: 'Settings',
      inventory: 'Inventory',
      chat: 'Chat',
      notifications: 'Notifications',
    },
    errors: {
      walletConnection: 'Error connecting wallet',
      sceneLoad: 'Error loading scene',
      playerMove: 'Error moving player',
      networkError: 'Network error',
    },
  },
}; 