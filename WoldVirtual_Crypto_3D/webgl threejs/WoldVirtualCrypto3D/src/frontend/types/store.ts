import { User, Scene, Asset } from './services';

export interface ReflexState {
  // Estado de autenticación
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;

  // Estado de la escena
  currentScene: Scene | null;
  assets: Record<string, Asset>;
  objects: Record<string, any>;
  environment: string;
  lighting: {
    ambient: [number, number, number];
    directional: [number, number, number];
  };

  // Estado del jugador
  playerPosition: [number, number, number];
  playerRotation: [number, number, number];
  playerScale: [number, number, number];
  playerMode: 'first' | 'third';
  playerControls: {
    enabled: boolean;
    locked: boolean;
  };

  // Estado de la UI
  ui: {
    showLogin: boolean;
    showInventory: boolean;
    showSettings: boolean;
    showChat: boolean;
    notifications: Array<{
      id: string;
      type: 'info' | 'success' | 'warning' | 'error';
      message: string;
      duration?: number;
    }>;
  };

  // Acciones
  setUser: (user: User | null) => void;
  setAuthenticated: (isAuthenticated: boolean) => void;
  setLoading: (isLoading: boolean) => void;
  setError: (error: string | null) => void;
  setCurrentScene: (scene: Scene | null) => void;
  setAssets: (assets: Record<string, Asset>) => void;
  setObjects: (objects: Record<string, any>) => void;
  setEnvironment: (environment: string) => void;
  setLighting: (lighting: { ambient: [number, number, number]; directional: [number, number, number] }) => void;
  setPlayerPosition: (position: [number, number, number]) => void;
  setPlayerRotation: (rotation: [number, number, number]) => void;
  setPlayerScale: (scale: [number, number, number]) => void;
  setPlayerMode: (mode: 'first' | 'third') => void;
  setPlayerControls: (controls: { enabled: boolean; locked: boolean }) => void;
  setShowLogin: (show: boolean) => void;
  setShowInventory: (show: boolean) => void;
  setShowSettings: (show: boolean) => void;
  setShowChat: (show: boolean) => void;
  addNotification: (notification: { type: 'info' | 'success' | 'warning' | 'error'; message: string; duration?: number }) => void;
  removeNotification: (id: string) => void;
  reset: () => void;
} 