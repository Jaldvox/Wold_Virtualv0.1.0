// Tipos para las utilidades de geometría
export interface Vector3 {
  x: number;
  y: number;
  z: number;
}

export interface Quaternion {
  x: number;
  y: number;
  z: number;
  w: number;
}

export interface Euler {
  x: number;
  y: number;
  z: number;
  order?: 'XYZ' | 'YXZ' | 'ZXY' | 'ZYX' | 'YZX' | 'XZY';
}

// Tipos para las utilidades de animación
export interface AnimationState {
  name: string;
  weight: number;
  timeScale: number;
  loop: boolean;
  clampWhenFinished: boolean;
  duration: number;
  startTime: number;
  endTime: number;
}

export interface AnimationTransition {
  from: string;
  to: string;
  duration: number;
  easing: string;
}

// Tipos para las utilidades de física
export interface PhysicsBody {
  mass: number;
  velocity: Vector3;
  acceleration: Vector3;
  force: Vector3;
  position: Vector3;
  rotation: Quaternion;
  scale: Vector3;
  isStatic: boolean;
  isKinematic: boolean;
  restitution: number;
  friction: number;
  linearDamping: number;
  angularDamping: number;
}

// Tipos para las utilidades de colisión
export interface Collider {
  type: 'box' | 'sphere' | 'cylinder' | 'capsule' | 'mesh';
  size: Vector3;
  offset: Vector3;
  rotation: Quaternion;
  isTrigger: boolean;
  layer: number;
  mask: number;
}

// Tipos para las utilidades de red
export interface NetworkMessage {
  type: string;
  data: any;
  timestamp: number;
  sender: string;
  target?: string;
}

export interface NetworkState {
  isConnected: boolean;
  latency: number;
  packetLoss: number;
  bandwidth: number;
  lastUpdate: number;
}

// Tipos para las utilidades de audio
export interface AudioSource {
  id: string;
  url: string;
  volume: number;
  pitch: number;
  loop: boolean;
  spatialBlend: number;
  minDistance: number;
  maxDistance: number;
  rolloffMode: 'linear' | 'logarithmic' | 'custom';
  position: Vector3;
  rotation: Quaternion;
}

// Tipos para las utilidades de partículas
export interface ParticleSystem {
  id: string;
  maxParticles: number;
  duration: number;
  startLifetime: number;
  startSpeed: number;
  startSize: number;
  startColor: string;
  gravityModifier: number;
  emissionRate: number;
  shape: {
    type: 'sphere' | 'box' | 'cone' | 'circle';
    radius?: number;
    size?: Vector3;
    angle?: number;
  };
  position: Vector3;
  rotation: Quaternion;
  scale: Vector3;
}

// Tipos para las utilidades de efectos
export interface PostProcessEffect {
  type: 'bloom' | 'chromaticAberration' | 'depthOfField' | 'motionBlur' | 'ssao';
  enabled: boolean;
  intensity: number;
  threshold?: number;
  radius?: number;
  samples?: number;
  color?: string;
  distance?: number;
  focusDistance?: number;
  focalLength?: number;
  bokehScale?: number;
  height?: number;
  luminanceThreshold?: number;
  luminanceSmoothing?: number;
} 