import React, { Component, ErrorInfo, ReactNode } from 'react';
import { motion } from 'framer-motion';

interface Props {
  children?: ReactNode;
  error?: string;
  onRetry?: () => void;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo): void {
    console.error('Error en la aplicación:', error, errorInfo);
  }

  render(): ReactNode {
    if (this.state.hasError || this.props.error) {
      const error = this.state.error || new Error(this.props.error);
      
      return (
        <div className="fixed inset-0 bg-gray-900 flex items-center justify-center z-50">
          <motion.div
            className="bg-gray-800 rounded-lg p-8 max-w-md w-full mx-4"
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
          >
            <div className="text-center">
              <motion.div
                className="w-16 h-16 bg-red-500 rounded-full mx-auto mb-4 flex items-center justify-center"
                initial={{ rotate: 0 }}
                animate={{ rotate: 360 }}
                transition={{ duration: 0.5 }}
              >
                <svg
                  className="w-8 h-8 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                  />
                </svg>
              </motion.div>

              <h2 className="text-2xl font-bold text-white mb-2">
                ¡Ups! Algo salió mal
              </h2>

              <p className="text-gray-400 mb-4">
                {error.message || 'Ha ocurrido un error inesperado'}
              </p>

              {this.props.onRetry && (
                <button
                  onClick={this.props.onRetry}
                  className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors duration-200"
                >
                  Intentar de nuevo
                </button>
              )}

              <button
                onClick={() => window.location.reload()}
                className="mt-4 text-gray-400 hover:text-white transition-colors duration-200 block mx-auto"
              >
                Recargar página
              </button>
            </div>
          </motion.div>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary; 