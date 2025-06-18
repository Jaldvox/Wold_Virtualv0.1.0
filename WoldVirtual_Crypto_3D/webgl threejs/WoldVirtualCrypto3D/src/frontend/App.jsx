import React, { useEffect, useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { Suspense } from 'react';
import MetaverseCore from './components/three/core/MetaverseCore';
import AuthService from './services/auth/AuthService';
import SyncService from './services/sync/SyncService';
import ContentService from './services/content/ContentService';
import Web3Service from './services/blockchain/Web3Service';

// Componentes de UI
import LoginModal from './components/ui/LoginModal';
import LoadingScreen from './components/ui/LoadingScreen';
import ErrorBoundary from './components/ui/ErrorBoundary';

function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showLogin, setShowLogin] = useState(false);

  useEffect(() => {
    initializeServices();
  }, []);

  const initializeServices = async () => {
    try {
      setIsLoading(true);
      setError(null);

      // Inicializar servicios en paralelo
      const [web3Initialized, authInitialized, syncInitialized, contentInitialized] = await Promise.all([
        Web3Service.initialize(),
        AuthService.initialize(),
        SyncService.initialize(),
        ContentService.initialize()
      ]);

      if (!web3Initialized) {
        throw new Error('Error inicializando Web3Service');
      }

      if (!authInitialized) {
        setShowLogin(true);
      }

      if (!syncInitialized) {
        throw new Error('Error inicializando SyncService');
      }

      if (!contentInitialized) {
        throw new Error('Error inicializando ContentService');
      }

      setIsLoading(false);
    } catch (error) {
      console.error('Error inicializando servicios:', error);
      setError(error.message);
      setIsLoading(false);
    }
  };

  const handleLogin = async () => {
    try {
      setIsLoading(true);
      await AuthService.loginWithWallet();
      setShowLogin(false);
      setIsLoading(false);
    } catch (error) {
      console.error('Error en login:', error);
      setError(error.message);
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return <LoadingScreen />;
  }

  if (error) {
    return (
      <ErrorBoundary
        error={error}
        onRetry={initializeServices}
      />
    );
  }

  return (
    <ErrorBoundary>
      <div className="app">
        <Canvas
          shadows
          camera={{
            position: [0, 5, 10],
            fov: 75,
            near: 0.1,
            far: 1000
          }}
        >
          <Suspense fallback={null}>
            <MetaverseCore />
          </Suspense>
        </Canvas>

        {showLogin && (
          <LoginModal
            onLogin={handleLogin}
            onClose={() => setShowLogin(false)}
          />
        )}
      </div>
    </ErrorBoundary>
  );
}

export default App;