import React, { useRef, useEffect } from 'react';
import { useThree } from '@react-three/fiber';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

const Avatar = ({ position, rotation }) => {
  const { scene } = useThree();
  const avatarRef = useRef();

  useEffect(() => {
    const loader = new GLTFLoader();
    loader.load('/path/to/avatar/model.glb', (gltf) => {
      const avatar = gltf.scene;
      avatar.position.set(...position);
      avatar.rotation.set(...rotation);
      scene.add(avatar);
      avatarRef.current = avatar;
    });

    return () => {
      if (avatarRef.current) {
        scene.remove(avatarRef.current);
      }
    };
  }, [position, rotation, scene]);

  return null;
};

export default Avatar;