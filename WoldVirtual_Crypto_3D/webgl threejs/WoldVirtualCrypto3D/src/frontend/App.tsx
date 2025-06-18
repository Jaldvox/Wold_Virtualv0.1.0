import React from 'react';
import { ThemeProvider } from './providers/ThemeProvider';
import { I18nProvider } from './providers/I18nProvider';
import { translations } from './i18n/translations';
import { LoadingScreen } from './components/ui/LoadingScreen';
import { ErrorBoundary } from './components/ui/ErrorBoundary';
import { useReflexStore } from './store/useReflexStore';
import { AuthService } from './services/auth/AuthService';
import { Web3Service } from './services/blockchain/Web3Service';
import { SyncService } from './services/sync/SyncService';
import { ContentService } from './services/content/ContentService';
import AppRoutes from './routes';

const App: React.FC = () => {
  const {
    isLoading,
    error,
    setLoading,
    setError,
  } = useReflexStore();

  // Inicializar servicios
  const initializeServices = async () => {
    try {
      setLoading(true);
      await Promise.all([
        AuthService.initialize(),
        Web3Service.initialize(),
        SyncService.initialize(),
        ContentService.initialize(),
      ]);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error desconocido');
    } finally {
      setLoading(false);
    }
  };

  // Inicializar servicios al montar
  React.useEffect(() => {
    initializeServices();
  }, []);

  if (isLoading) {
    return <LoadingScreen />;
  }

  if (error) {
    return <ErrorBoundary error={error} />;
  }

  return (
    <ThemeProvider>
      <I18nProvider translations={translations}>
        <ErrorBoundary>
          <AppRoutes />
        </ErrorBoundary>
      </I18nProvider>
    </ThemeProvider>
  );
};

export default App; 