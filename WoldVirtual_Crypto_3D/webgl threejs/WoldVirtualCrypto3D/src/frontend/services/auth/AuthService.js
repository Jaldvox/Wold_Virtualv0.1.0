import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import Web3Service from '../blockchain/Web3Service';

// Store para el estado de autenticación
const useAuthStore = create(
  persist(
    (set) => ({
      user: null,
      token: null,
      isAuthenticated: false,
      setUser: (user) => set({ user, isAuthenticated: !!user }),
      setToken: (token) => set({ token }),
      logout: () => set({ user: null, token: null, isAuthenticated: false })
    }),
    {
      name: 'auth-storage'
    }
  )
);

class AuthService {
  constructor() {
    this.store = useAuthStore;
    this.web3Service = Web3Service;
  }

  async initialize() {
    try {
      // Verificar si hay un token guardado
      const token = this.store.getState().token;
      if (token) {
        // Validar token con el backend
        const isValid = await this.validateToken(token);
        if (!isValid) {
          this.logout();
        }
      }
      return true;
    } catch (error) {
      console.error('Error inicializando AuthService:', error);
      return false;
    }
  }

  async loginWithWallet() {
    try {
      // Conectar wallet
      const accounts = await this.web3Service.initialize();
      if (!accounts || accounts.length === 0) {
        throw new Error('No se pudo conectar a la wallet');
      }

      const address = accounts[0];

      // Obtener mensaje para firmar
      const response = await fetch(`${process.env.VITE_API_URL}/auth/nonce`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ address })
      });

      const { nonce } = await response.json();

      // Firmar mensaje
      const signature = await this.web3Service.provider.getSigner().signMessage(nonce);

      // Autenticar con el backend
      const authResponse = await fetch(`${process.env.VITE_API_URL}/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ address, signature })
      });

      const { user, token } = await authResponse.json();

      // Guardar estado
      this.store.getState().setUser(user);
      this.store.getState().setToken(token);

      return { user, token };
    } catch (error) {
      console.error('Error en login con wallet:', error);
      throw error;
    }
  }

  async validateToken(token) {
    try {
      const response = await fetch(`${process.env.VITE_API_URL}/auth/validate`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      return response.ok;
    } catch (error) {
      console.error('Error validando token:', error);
      return false;
    }
  }

  async refreshToken() {
    try {
      const token = this.store.getState().token;
      if (!token) return false;

      const response = await fetch(`${process.env.VITE_API_URL}/auth/refresh`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      if (!response.ok) {
        throw new Error('Error refrescando token');
      }

      const { newToken } = await response.json();
      this.store.getState().setToken(newToken);

      return true;
    } catch (error) {
      console.error('Error refrescando token:', error);
      return false;
    }
  }

  logout() {
    this.store.getState().logout();
  }

  getUser() {
    return this.store.getState().user;
  }

  getToken() {
    return this.store.getState().token;
  }

  isAuthenticated() {
    return this.store.getState().isAuthenticated;
  }

  // Método para obtener headers con token
  getAuthHeaders() {
    const token = this.getToken();
    return token ? { 'Authorization': `Bearer ${token}` } : {};
  }
}

export default new AuthService(); 