import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface LoginModalProps {
  onLogin: () => Promise<void>;
  onClose: () => void;
}

const LoginModal: React.FC<LoginModalProps> = ({ onLogin, onClose }) => {
  return (
    <AnimatePresence>
      <motion.div
        className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
      >
        <motion.div
          className="bg-gray-900 rounded-lg p-8 max-w-md w-full mx-4"
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          exit={{ scale: 0.9, opacity: 0 }}
        >
          <div className="text-center">
            <h2 className="text-3xl font-bold text-white mb-4">
              Conecta tu Wallet
            </h2>
            <p className="text-gray-400 mb-8">
              Conecta tu wallet para acceder al metaverso y comenzar tu aventura
            </p>

            <button
              onClick={onLogin}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors duration-200 flex items-center justify-center space-x-2"
            >
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                />
              </svg>
              <span>Conectar con MetaMask</span>
            </button>

            <button
              onClick={onClose}
              className="mt-4 text-gray-400 hover:text-white transition-colors duration-200"
            >
              Cancelar
            </button>
          </div>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
};

export default LoginModal; 