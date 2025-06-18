import React, { useEffect, useRef } from 'react';
import { useThree, useFrame } from '@react-three/fiber';
import { PointerLockControls, FirstPersonControls } from '@react-three/drei';
import * as THREE from 'three';

const PlayerControls = ({
  mode = 'firstPerson', // 'firstPerson' o 'thirdPerson'
  target,
  onMove,
  onRotate,
  enabled = true
}) => {
  const { camera, gl } = useThree();
  const controlsRef = useRef();
  const velocity = useRef(new THREE.Vector3());
  const direction = useRef(new THREE.Vector3());
  const moveSpeed = 5;
  const rotateSpeed = 0.002;

  // Configuración inicial
  useEffect(() => {
    if (controlsRef.current) {
      controlsRef.current.addEventListener('lock', () => {
        // Habilitar controles cuando el puntero está bloqueado
        enabled = true;
      });

      controlsRef.current.addEventListener('unlock', () => {
        // Deshabilitar controles cuando el puntero está desbloqueado
        enabled = false;
      });
    }
  }, []);

  // Actualización por frame
  useFrame((state, delta) => {
    if (!enabled || !controlsRef.current) return;

    // Actualizar velocidad y dirección
    velocity.current.x -= velocity.current.x * 10.0 * delta;
    velocity.current.z -= velocity.current.z * 10.0 * delta;
    velocity.current.y -= 9.8 * delta; // Gravedad

    direction.current.z = Number(moveForward) - Number(moveBackward);
    direction.current.x = Number(moveRight) - Number(moveLeft);
    direction.current.normalize();

    if (moveForward || moveBackward) {
      velocity.current.z -= direction.current.z * moveSpeed * delta;
    }
    if (moveLeft || moveRight) {
      velocity.current.x -= direction.current.x * moveSpeed * delta;
    }

    // Aplicar movimiento
    controlsRef.current.moveRight(-velocity.current.x * delta);
    controlsRef.current.moveForward(-velocity.current.z * delta);

    // Actualizar posición de la cámara en modo tercera persona
    if (mode === 'thirdPerson' && target) {
      const idealOffset = new THREE.Vector3(0, 2, -5);
      idealOffset.applyQuaternion(camera.quaternion);
      idealOffset.add(target.position);
      
      camera.position.lerp(idealOffset, 0.1);
      camera.lookAt(target.position);
    }

    // Notificar cambios
    if (onMove) {
      onMove({
        position: camera.position,
        rotation: camera.rotation
      });
    }
  });

  // Manejo de eventos de teclado
  const moveForward = useRef(false);
  const moveBackward = useRef(false);
  const moveLeft = useRef(false);
  const moveRight = useRef(false);

  useEffect(() => {
    const onKeyDown = (event) => {
      switch (event.code) {
        case 'KeyW':
          moveForward.current = true;
          break;
        case 'KeyS':
          moveBackward.current = true;
          break;
        case 'KeyA':
          moveLeft.current = true;
          break;
        case 'KeyD':
          moveRight.current = true;
          break;
      }
    };

    const onKeyUp = (event) => {
      switch (event.code) {
        case 'KeyW':
          moveForward.current = false;
          break;
        case 'KeyS':
          moveBackward.current = false;
          break;
        case 'KeyA':
          moveLeft.current = false;
          break;
        case 'KeyD':
          moveRight.current = false;
          break;
      }
    };

    document.addEventListener('keydown', onKeyDown);
    document.addEventListener('keyup', onKeyUp);

    return () => {
      document.removeEventListener('keydown', onKeyDown);
      document.removeEventListener('keyup', onKeyUp);
    };
  }, []);

  return mode === 'firstPerson' ? (
    <PointerLockControls ref={controlsRef} />
  ) : (
    <FirstPersonControls
      ref={controlsRef}
      activeLook={true}
      movementSpeed={moveSpeed}
      lookSpeed={rotateSpeed}
    />
  );
};

export default PlayerControls; 