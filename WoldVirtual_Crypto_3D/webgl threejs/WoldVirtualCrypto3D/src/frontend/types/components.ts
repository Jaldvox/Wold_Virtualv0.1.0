import { ReactNode } from 'react';
import { User } from './services';

// Tipos para LoginModal
export interface LoginModalProps {
  onLogin: (user: User) => void;
  onClose: () => void;
}

// Tipos para LoadingScreen
export interface LoadingScreenProps {
  message?: string;
}

// Tipos para ErrorBoundary
export interface ErrorBoundaryProps {
  children: ReactNode;
  fallback?: ReactNode;
}

export interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
}

// Tipos para Avatar
export interface AvatarProps {
  position?: [number, number, number];
  rotation?: [number, number, number];
  scale?: [number, number, number];
  modelUrl?: string;
  animationState?: string;
  onAnimationComplete?: () => void;
  isPlayer?: boolean;
}

// Tipos para PlayerControls
export interface PlayerControlsProps {
  mode: 'first' | 'third';
  target?: [number, number, number];
  onMove?: (position: [number, number, number]) => void;
  onRotate?: (rotation: [number, number, number]) => void;
  enabled?: boolean;
}

// Tipos para MetaverseScene
export interface MetaverseSceneProps {
  environment?: string;
  fogColor?: string;
  fogDensity?: number;
  ambientLightIntensity?: number;
  directionalLightIntensity?: number;
  bloomIntensity?: number;
  chromaticAberrationIntensity?: number;
  onSceneReady?: () => void;
}

// Tipos para MetaverseCore
export interface MetaverseCoreProps {
  onReady?: () => void;
  onError?: (error: Error) => void;
} 