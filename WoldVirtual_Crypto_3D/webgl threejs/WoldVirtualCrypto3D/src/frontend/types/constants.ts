// Constantes de la aplicación
export const APP_NAME = 'Wold Virtual Crypto 3D';
export const APP_VERSION = '0.0.1';
export const APP_DESCRIPTION = 'Un metaverso 3D basado en blockchain';
export const APP_AUTHOR = 'Wold Virtual';
export const APP_LICENSE = 'MIT';

// Constantes de la red
export const NETWORK = {
  MAINNET: 'mainnet',
  TESTNET: 'testnet',
  LOCAL: 'local'
} as const;

export const RPC_URLS = {
  [NETWORK.MAINNET]: 'https://mainnet.infura.io/v3/YOUR-PROJECT-ID',
  [NETWORK.TESTNET]: 'https://goerli.infura.io/v3/YOUR-PROJECT-ID',
  [NETWORK.LOCAL]: 'http://localhost:8545'
} as const;

export const CHAIN_IDS = {
  [NETWORK.MAINNET]: 1,
  [NETWORK.TESTNET]: 5,
  [NETWORK.LOCAL]: 1337
} as const;

// Constantes de los contratos
export const CONTRACT_ADDRESSES = {
  [NETWORK.MAINNET]: {
    NFT: '0x...',
    TOKEN: '0x...'
  },
  [NETWORK.TESTNET]: {
    NFT: '0x...',
    TOKEN: '0x...'
  },
  [NETWORK.LOCAL]: {
    NFT: '0x...',
    TOKEN: '0x...'
  }
} as const;

// Constantes de la escena
export const SCENE = {
  DEFAULT_ENVIRONMENT: 'sunset',
  DEFAULT_FOG_COLOR: '#000000',
  DEFAULT_FOG_DENSITY: 0.01,
  DEFAULT_AMBIENT_LIGHT_INTENSITY: 0.5,
  DEFAULT_DIRECTIONAL_LIGHT_INTENSITY: 1,
  DEFAULT_BLOOM_INTENSITY: 0.5,
  DEFAULT_CHROMATIC_ABERRATION_INTENSITY: 0.005,
  DEFAULT_GRAVITY: -9.81,
  DEFAULT_FRICTION: 0.1,
  DEFAULT_JUMP_FORCE: 5,
  DEFAULT_MOVE_SPEED: 5,
  DEFAULT_ROTATION_SPEED: 0.1,
  DEFAULT_CAMERA_FOV: 75,
  DEFAULT_CAMERA_NEAR: 0.1,
  DEFAULT_CAMERA_FAR: 1000,
  DEFAULT_CAMERA_POSITION: [0, 2, 5],
  DEFAULT_CAMERA_LOOK_AT: [0, 0, 0]
} as const;

// Constantes de la UI
export const UI = {
  DEFAULT_THEME: 'dark',
  DEFAULT_LANGUAGE: 'es',
  DEFAULT_FONT_FAMILY: 'Inter, sans-serif',
  DEFAULT_FONT_SIZE: 16,
  DEFAULT_BORDER_RADIUS: 8,
  DEFAULT_SPACING: 16,
  DEFAULT_ANIMATION_DURATION: 0.3,
  DEFAULT_TRANSITION: 'all 0.3s ease',
  DEFAULT_SHADOW: '0 4px 6px rgba(0, 0, 0, 0.1)',
  DEFAULT_Z_INDEX: {
    MODAL: 1000,
    TOOLTIP: 900,
    DROPDOWN: 800,
    HEADER: 700,
    FOOTER: 600
  }
} as const;

// Constantes de los eventos
export const EVENTS = {
  // Eventos de autenticación
  AUTH: {
    LOGIN: 'auth:login',
    LOGOUT: 'auth:logout',
    ERROR: 'auth:error'
  },
  // Eventos de la escena
  SCENE: {
    LOAD: 'scene:load',
    UNLOAD: 'scene:unload',
    UPDATE: 'scene:update',
    ERROR: 'scene:error'
  },
  // Eventos del jugador
  PLAYER: {
    MOVE: 'player:move',
    ROTATE: 'player:rotate',
    JUMP: 'player:jump',
    INTERACT: 'player:interact',
    ERROR: 'player:error'
  },
  // Eventos de la UI
  UI: {
    SHOW_MODAL: 'ui:showModal',
    HIDE_MODAL: 'ui:hideModal',
    SHOW_TOOLTIP: 'ui:showTooltip',
    HIDE_TOOLTIP: 'ui:hideTooltip',
    SHOW_NOTIFICATION: 'ui:showNotification',
    HIDE_NOTIFICATION: 'ui:hideNotification',
    ERROR: 'ui:error'
  },
  // Eventos de la red
  NETWORK: {
    CONNECT: 'network:connect',
    DISCONNECT: 'network:disconnect',
    ERROR: 'network:error'
  }
} as const;

// Constantes de las animaciones
export const ANIMATIONS = {
  IDLE: 'idle',
  WALK: 'walk',
  RUN: 'run',
  JUMP: 'jump',
  FALL: 'fall',
  LAND: 'land',
  ATTACK: 'attack',
  HIT: 'hit',
  DEATH: 'death'
} as const;

// Constantes de las colisiones
export const COLLISION_LAYERS = {
  DEFAULT: 0,
  PLAYER: 1,
  ENEMY: 2,
  ITEM: 3,
  TRIGGER: 4,
  ENVIRONMENT: 5
} as const;

// Constantes de los efectos
export const EFFECTS = {
  BLOOM: 'bloom',
  CHROMATIC_ABERRATION: 'chromaticAberration',
  DEPTH_OF_FIELD: 'depthOfField',
  MOTION_BLUR: 'motionBlur',
  SSAO: 'ssao'
} as const;

// Constantes de los sonidos
export const SOUNDS = {
  AMBIENT: 'ambient',
  MUSIC: 'music',
  FOOTSTEPS: 'footsteps',
  JUMP: 'jump',
  LAND: 'land',
  ATTACK: 'attack',
  HIT: 'hit',
  DEATH: 'death',
  UI: {
    CLICK: 'ui:click',
    HOVER: 'ui:hover',
    NOTIFICATION: 'ui:notification'
  }
} as const; 