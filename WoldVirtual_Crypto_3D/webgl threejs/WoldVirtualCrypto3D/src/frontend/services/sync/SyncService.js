import { io } from 'socket.io-client';
import { create } from 'zustand';

// Store para el estado de sincronización
const useSyncStore = create((set) => ({
  connected: false,
  users: {},
  objects: {},
  setConnected: (connected) => set({ connected }),
  addUser: (user) => set((state) => ({
    users: { ...state.users, [user.id]: user }
  })),
  removeUser: (userId) => set((state) => {
    const { [userId]: removed, ...users } = state.users;
    return { users };
  }),
  updateUser: (userId, data) => set((state) => ({
    users: {
      ...state.users,
      [userId]: { ...state.users[userId], ...data }
    }
  })),
  addObject: (object) => set((state) => ({
    objects: { ...state.objects, [object.id]: object }
  })),
  removeObject: (objectId) => set((state) => {
    const { [objectId]: removed, ...objects } = state.objects;
    return { objects };
  }),
  updateObject: (objectId, data) => set((state) => ({
    objects: {
      ...state.objects,
      [objectId]: { ...state.objects[objectId], ...data }
    }
  }))
}));

class SyncService {
  constructor() {
    this.socket = null;
    this.store = useSyncStore;
    this.initialized = false;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 5;
  }

  async initialize() {
    try {
      // Inicializar Socket.IO
      this.socket = io(process.env.VITE_WS_URL, {
        transports: ['websocket'],
        reconnection: true,
        reconnectionAttempts: this.maxReconnectAttempts,
        reconnectionDelay: 1000
      });

      // Configurar eventos
      this.setupEventListeners();

      this.initialized = true;
      return true;
    } catch (error) {
      console.error('Error inicializando SyncService:', error);
      return false;
    }
  }

  setupEventListeners() {
    if (!this.socket) return;

    // Eventos de conexión
    this.socket.on('connect', () => {
      this.store.getState().setConnected(true);
      this.reconnectAttempts = 0;
    });

    this.socket.on('disconnect', () => {
      this.store.getState().setConnected(false);
    });

    // Eventos de usuarios
    this.socket.on('user:join', (user) => {
      this.store.getState().addUser(user);
    });

    this.socket.on('user:leave', (userId) => {
      this.store.getState().removeUser(userId);
    });

    this.socket.on('user:update', ({ userId, data }) => {
      this.store.getState().updateUser(userId, data);
    });

    // Eventos de objetos
    this.socket.on('object:create', (object) => {
      this.store.getState().addObject(object);
    });

    this.socket.on('object:remove', (objectId) => {
      this.store.getState().removeObject(objectId);
    });

    this.socket.on('object:update', ({ objectId, data }) => {
      this.store.getState().updateObject(objectId, data);
    });
  }

  // Métodos para enviar actualizaciones
  updateUserPosition(userId, position) {
    if (!this.initialized) return;
    this.socket.emit('user:position', { userId, position });
  }

  updateUserRotation(userId, rotation) {
    if (!this.initialized) return;
    this.socket.emit('user:rotation', { userId, rotation });
  }

  updateObjectPosition(objectId, position) {
    if (!this.initialized) return;
    this.socket.emit('object:position', { objectId, position });
  }

  updateObjectRotation(objectId, rotation) {
    if (!this.initialized) return;
    this.socket.emit('object:rotation', { objectId, rotation });
  }

  // Métodos para interacciones
  createObject(object) {
    if (!this.initialized) return;
    this.socket.emit('object:create', object);
  }

  removeObject(objectId) {
    if (!this.initialized) return;
    this.socket.emit('object:remove', objectId);
  }

  // Métodos para obtener estado
  getConnectedUsers() {
    return this.store.getState().users;
  }

  getObjects() {
    return this.store.getState().objects;
  }

  isConnected() {
    return this.store.getState().connected;
  }

  // Limpieza
  cleanup() {
    if (this.socket) {
      this.socket.disconnect();
      this.socket = null;
    }
    this.initialized = false;
  }
}

export default new SyncService(); 