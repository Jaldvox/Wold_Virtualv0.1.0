import React from 'react';
import { useReflexStore } from '../store/useReflexStore';
import { useI18n } from '../providers/I18nProvider';
import { useTheme } from '../providers/ThemeProvider';

const Profile: React.FC = () => {
  const { t } = useI18n();
  const { theme, toggleTheme } = useTheme();
  const { user, setUser } = useReflexStore();

  if (!user) {
    return (
      <div className="flex items-center justify-center h-screen">
        <p className="text-xl">{t('auth.login')}</p>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-2xl font-bold">{t('profile.title')}</h1>
          <button
            onClick={toggleTheme}
            className="px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600"
          >
            {theme === 'dark' ? t('theme.light') : t('theme.dark')}
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
              {t('profile.wallet')}
            </label>
            <p className="mt-1 text-sm text-gray-900 dark:text-gray-100">
              {user.wallet}
            </p>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
              {t('profile.balance')}
            </label>
            <p className="mt-1 text-sm text-gray-900 dark:text-gray-100">
              {user.balance} ETH
            </p>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
              {t('profile.nfts')}
            </label>
            <div className="mt-2 grid grid-cols-2 gap-4">
              {user.nfts.map((nft, index) => (
                <div
                  key={index}
                  className="border rounded-lg p-4 dark:border-gray-700"
                >
                  <img
                    src={nft.image}
                    alt={nft.name}
                    className="w-full h-32 object-cover rounded"
                  />
                  <p className="mt-2 text-sm font-medium">{nft.name}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile; 