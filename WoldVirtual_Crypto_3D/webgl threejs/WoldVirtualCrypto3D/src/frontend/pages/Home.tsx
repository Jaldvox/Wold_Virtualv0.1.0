import React from 'react';
import { Canvas } from '@react-three/fiber';
import { useReflexStore } from '../store/useReflexStore';
import { useI18n } from '../providers/I18nProvider';
import { MetaverseCore } from '../components/three/core/MetaverseCore';
import { PlayerControls } from '../components/three/controls/PlayerControls';
import { Avatar } from '../components/three/objects/Avatar';

const Home: React.FC = () => {
  const { t } = useI18n();
  const { currentScene, playerPosition, playerRotation, playerScale } = useReflexStore();

  return (
    <div className="h-screen w-full">
      <Canvas
        shadows
        camera={{
          position: [0, 5, 10],
          fov: 75,
          near: 0.1,
          far: 1000
        }}
      >
        <ambientLight intensity={0.5} />
        <directionalLight
          position={[10, 10, 5]}
          intensity={1}
          castShadow
        />
        
        <MetaverseCore />
        <PlayerControls />
        <Avatar
          position={playerPosition}
          rotation={playerRotation}
          scale={playerScale}
        />
      </Canvas>
    </div>
  );
};

export default Home; 