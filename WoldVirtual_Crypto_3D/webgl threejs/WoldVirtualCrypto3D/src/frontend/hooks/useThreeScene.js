import { useEffect, useRef } from 'react';
import * as THREE from 'three';
import { Reflex3DBridge } from '../components/three/core/Reflex3DBridge';

const useThreeScene = (onSceneReady) => {
  const sceneRef = useRef();
  const rendererRef = useRef();
  const cameraRef = useRef();
  const clock = new THREE.Clock();

  useEffect(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    sceneRef.current.appendChild(renderer.domElement);

    camera.position.z = 5;

    const animate = () => {
      requestAnimationFrame(animate);
      const delta = clock.getDelta();
      // Update scene elements here
      if (onSceneReady) {
        onSceneReady(scene, camera, renderer, delta);
      }
      renderer.render(scene, camera);
    };

    animate();

    // Cleanup on unmount
    return () => {
      sceneRef.current.removeChild(renderer.domElement);
      renderer.dispose();
    };
  }, [onSceneReady]);

  return { sceneRef, cameraRef, rendererRef };
};

export default useThreeScene;