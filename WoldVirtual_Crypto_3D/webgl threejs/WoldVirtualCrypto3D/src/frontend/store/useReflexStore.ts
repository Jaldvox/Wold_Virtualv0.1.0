import { create, StateCreator } from 'zustand';
import { ReflexState } from '../types/store';
import { User, Scene, Asset } from '../types/services';

// Tipos para las notificaciones
type NotificationType = 'info' | 'success' | 'warning' | 'error';
type Notification = {
  id: string;
  type: NotificationType;
  message: string;
  duration?: number;
};

// Estado inicial
const initialState = {
  user: null as User | null,
  isAuthenticated: false,
  isLoading: false,
  error: null as string | null,
  currentScene: null as Scene | null,
  assets: {} as Record<string, Asset>,
  objects: {} as Record<string, any>,
  environment: 'sunset' as const,
  lighting: {
    ambient: [1, 1, 1] as [number, number, number],
    directional: [1, 1, 1] as [number, number, number],
  },
  playerPosition: [0, 2, 5] as [number, number, number],
  playerRotation: [0, 0, 0] as [number, number, number],
  playerScale: [1, 1, 1] as [number, number, number],
  playerMode: 'third' as const,
  playerControls: {
    enabled: true,
    locked: false,
  },
  ui: {
    showLogin: false,
    showInventory: false,
    showSettings: false,
    showChat: false,
    notifications: [] as Notification[],
  },
};

// Store
export const useReflexStore = create<ReflexState>((set: StateCreator<ReflexState>['set']) => ({
  ...initialState,

  // Acciones de autenticación
  setUser: (user: User | null) => set({ user }),
  setAuthenticated: (isAuthenticated: boolean) => set({ isAuthenticated }),
  setLoading: (isLoading: boolean) => set({ isLoading }),
  setError: (error: string | null) => set({ error }),

  // Acciones de escena
  setCurrentScene: (scene: Scene | null) => set({ currentScene: scene }),
  setAssets: (assets: Record<string, Asset>) => set({ assets }),
  setObjects: (objects: Record<string, any>) => set({ objects }),
  setEnvironment: (environment: string) => set({ environment }),
  setLighting: (lighting: { ambient: [number, number, number]; directional: [number, number, number] }) => 
    set({ lighting }),

  // Acciones del jugador
  setPlayerPosition: (position: [number, number, number]) => set({ playerPosition: position }),
  setPlayerRotation: (rotation: [number, number, number]) => set({ playerRotation: rotation }),
  setPlayerScale: (scale: [number, number, number]) => set({ playerScale: scale }),
  setPlayerMode: (mode: 'first' | 'third') => set({ playerMode: mode }),
  setPlayerControls: (controls: { enabled: boolean; locked: boolean }) => 
    set({ playerControls: controls }),

  // Acciones de UI
  setShowLogin: (show: boolean) => 
    set((state: ReflexState) => ({ ui: { ...state.ui, showLogin: show } })),
  setShowInventory: (show: boolean) => 
    set((state: ReflexState) => ({ ui: { ...state.ui, showInventory: show } })),
  setShowSettings: (show: boolean) => 
    set((state: ReflexState) => ({ ui: { ...state.ui, showSettings: show } })),
  setShowChat: (show: boolean) => 
    set((state: ReflexState) => ({ ui: { ...state.ui, showChat: show } })),

  // Acciones de notificaciones
  addNotification: (notification: Omit<Notification, 'id'>) => 
    set((state: ReflexState) => ({
      ui: {
        ...state.ui,
        notifications: [
          ...state.ui.notifications,
          { ...notification, id: Date.now().toString() }
        ]
      }
    })),
  removeNotification: (id: string) => 
    set((state: ReflexState) => ({
      ui: {
        ...state.ui,
        notifications: state.ui.notifications.filter((n: Notification) => n.id !== id)
      }
    })),

  // Reset del estado
  reset: () => set(initialState),
})); 