import React, { useEffect, useRef } from 'react';
import { Canvas } from '@react-three/fiber';
import { Reflex3DBridge } from './three/core/Reflex3DBridge';
import { WorldScene } from './three/scenes/WorldScene';
import { AvatarScene } from './three/scenes/AvatarScene';

const MetaverseScene = () => {
  const canvasRef = useRef();

  useEffect(() => {
    const bridge = new Reflex3DBridge();
    bridge.initialize();

    return () => {
      bridge.cleanup();
    };
  }, []);

  return (
    <Canvas ref={canvasRef}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 10, 7.5]} intensity={1} />
      <WorldScene />
      <AvatarScene />
    </Canvas>
  );
};

export default MetaverseScene;