import React, { useEffect, useRef } from 'react';
import { Canvas, useThree, useFrame } from '@react-three/fiber';
import { Environment, OrbitControls, PerspectiveCamera } from '@react-three/drei';
import { EffectComposer, Bloom, ChromaticAberration } from '@react-three/postprocessing';
import { BlendFunction } from 'postprocessing';

// Componente para la gestión de la escena principal
const MetaverseScene = ({ reflexState, updateReflexState }) => {
  const { scene, camera } = useThree();
  const sceneRef = useRef();

  // Configuración inicial de la escena
  useEffect(() => {
    if (sceneRef.current) {
      // Configurar iluminación global
      scene.background = new THREE.Color(0x000000);
      scene.fog = new THREE.FogExp2(0x000000, 0.002);
    }
  }, [scene]);

  // Actualización por frame
  useFrame((state, delta) => {
    // Actualizar estado de la escena basado en reflexState
    if (reflexState.cameraPosition) {
      camera.position.set(
        reflexState.cameraPosition.x,
        reflexState.cameraPosition.y,
        reflexState.cameraPosition.z
      );
    }
  });

  return (
    <group ref={sceneRef}>
      {/* Iluminación */}
      <ambientLight intensity={0.5} />
      <directionalLight
        position={[10, 10, 5]}
        intensity={1}
        castShadow
        shadow-mapSize={[2048, 2048]}
      />

      {/* Efectos post-procesado */}
      <EffectComposer>
        <Bloom
          intensity={1.0}
          luminanceThreshold={0.9}
          luminanceSmoothing={0.025}
        />
        <ChromaticAberration
          blendFunction={BlendFunction.NORMAL}
          offset={[0.0005, 0.0005]}
        />
      </EffectComposer>

      {/* Controles de cámara */}
      <OrbitControls
        enableDamping
        dampingFactor={0.05}
        minDistance={5}
        maxDistance={50}
      />

      {/* Entorno */}
      <Environment preset="sunset" />
    </group>
  );
};

// Componente principal del metaverso
const MetaverseCore = ({ reflexState, updateReflexState }) => {
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <Canvas shadows>
        <PerspectiveCamera makeDefault position={[0, 5, 10]} />
        <MetaverseScene
          reflexState={reflexState}
          updateReflexState={updateReflexState}
        />
      </Canvas>
    </div>
  );
};

export default MetaverseCore; 