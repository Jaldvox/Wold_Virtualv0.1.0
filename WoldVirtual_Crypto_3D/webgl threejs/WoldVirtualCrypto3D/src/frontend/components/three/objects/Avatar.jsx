import React, { useEffect, useRef } from 'react';
import { useGLTF, useAnimations } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';

const Avatar = ({ 
  position = [0, 0, 0], 
  rotation = [0, 0, 0],
  scale = 1,
  modelUrl,
  animationState,
  onAnimationComplete,
  isPlayer = false
}) => {
  const group = useRef();
  const { scene, animations } = useGLTF(modelUrl);
  const { actions, names } = useAnimations(animations, group);

  // Configuración inicial del avatar
  useEffect(() => {
    if (group.current) {
      // Configurar sombras
      group.current.traverse((child) => {
        if (child.isMesh) {
          child.castShadow = true;
          child.receiveShadow = true;
        }
      });

      // Configurar materiales PBR
      group.current.traverse((child) => {
        if (child.isMesh) {
          child.material = new THREE.MeshStandardMaterial({
            ...child.material,
            roughness: 0.7,
            metalness: 0.2,
          });
        }
      });
    }
  }, [scene]);

  // Manejo de animaciones
  useEffect(() => {
    if (animationState && actions[animationState]) {
      const action = actions[animationState];
      action.reset().fadeIn(0.5).play();
      
      if (onAnimationComplete) {
        action.getMixer().addEventListener('finished', onAnimationComplete);
      }
    }
  }, [animationState, actions, onAnimationComplete]);

  // Actualización por frame
  useFrame((state, delta) => {
    if (group.current) {
      // Actualizar posición y rotación
      group.current.position.set(...position);
      group.current.rotation.set(...rotation);
      group.current.scale.set(scale, scale, scale);

      // Actualizar animaciones
      if (actions[animationState]) {
        actions[animationState].update(delta);
      }
    }
  });

  return (
    <group ref={group}>
      <primitive object={scene} />
    </group>
  );
};

export default Avatar; 