// Tipos para los eventos
export interface Event {
  type: string;
  data: any;
  timestamp: number;
  sender: string;
  target?: string;
}

// Eventos de autenticación
export interface AuthEvent extends Event {
  type: 'auth:login' | 'auth:logout' | 'auth:error';
  data: {
    user?: {
      id: string;
      address: string;
      username?: string;
      avatar?: string;
    };
    error?: {
      code: string;
      message: string;
    };
  };
}

// Eventos de la escena
export interface SceneEvent extends Event {
  type: 'scene:load' | 'scene:unload' | 'scene:update' | 'scene:error';
  data: {
    scene?: {
      id: string;
      name: string;
      description: string;
      objects: Array<{
        id: string;
        type: string;
        position: [number, number, number];
        rotation: [number, number, number];
        scale: [number, number, number];
      }>;
    };
    error?: {
      code: string;
      message: string;
    };
  };
}

// Eventos del jugador
export interface PlayerEvent extends Event {
  type: 'player:move' | 'player:rotate' | 'player:jump' | 'player:interact' | 'player:error';
  data: {
    position?: [number, number, number];
    rotation?: [number, number, number];
    velocity?: [number, number, number];
    animation?: string;
    error?: {
      code: string;
      message: string;
    };
  };
}

// Eventos de la UI
export interface UIEvent extends Event {
  type: 'ui:showModal' | 'ui:hideModal' | 'ui:showTooltip' | 'ui:hideTooltip' | 'ui:showNotification' | 'ui:hideNotification' | 'ui:error';
  data: {
    modal?: {
      id: string;
      type: string;
      content: any;
    };
    tooltip?: {
      id: string;
      content: string;
      position: [number, number];
    };
    notification?: {
      id: string;
      type: 'success' | 'warning' | 'error' | 'info';
      message: string;
      duration?: number;
    };
    error?: {
      code: string;
      message: string;
    };
  };
}

// Eventos de la red
export interface NetworkEvent extends Event {
  type: 'network:connect' | 'network:disconnect' | 'network:error';
  data: {
    status?: {
      isConnected: boolean;
      latency: number;
      packetLoss: number;
      bandwidth: number;
    };
    error?: {
      code: string;
      message: string;
    };
  };
}

// Eventos de las animaciones
export interface AnimationEvent extends Event {
  type: 'animation:start' | 'animation:end' | 'animation:error';
  data: {
    animation?: {
      name: string;
      duration: number;
      loop: boolean;
      weight: number;
    };
    error?: {
      code: string;
      message: string;
    };
  };
}

// Eventos de las colisiones
export interface CollisionEvent extends Event {
  type: 'collision:enter' | 'collision:exit' | 'collision:stay' | 'collision:error';
  data: {
    collision?: {
      object1: {
        id: string;
        type: string;
        layer: number;
      };
      object2: {
        id: string;
        type: string;
        layer: number;
      };
      point: [number, number, number];
      normal: [number, number, number];
      distance: number;
    };
    error?: {
      code: string;
      message: string;
    };
  };
}

// Eventos de los efectos
export interface EffectEvent extends Event {
  type: 'effect:enable' | 'effect:disable' | 'effect:update' | 'effect:error';
  data: {
    effect?: {
      type: 'bloom' | 'chromaticAberration' | 'depthOfField' | 'motionBlur' | 'ssao';
      enabled: boolean;
      intensity: number;
      params?: Record<string, any>;
    };
    error?: {
      code: string;
      message: string;
    };
  };
}

// Eventos de los sonidos
export interface SoundEvent extends Event {
  type: 'sound:play' | 'sound:stop' | 'sound:pause' | 'sound:resume' | 'sound:error';
  data: {
    sound?: {
      id: string;
      type: string;
      volume: number;
      pitch: number;
      loop: boolean;
      spatialBlend: number;
    };
    error?: {
      code: string;
      message: string;
    };
  };
}

// Unión de todos los tipos de eventos
export type GameEvent =
  | AuthEvent
  | SceneEvent
  | PlayerEvent
  | UIEvent
  | NetworkEvent
  | AnimationEvent
  | CollisionEvent
  | EffectEvent
  | SoundEvent; 