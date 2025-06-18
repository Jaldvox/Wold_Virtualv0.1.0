import * as THREE from 'three';
import { Environment } from '../objects/Environment';
import { LightingSystem } from '../lighting/LightingSystem';
import { Reflex3DBridge } from '../core/Reflex3DBridge';

export function WorldScene(reflexState) {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Set up environment
    const environment = new Environment();
    scene.add(environment);

    // Set up lighting
    const lightingSystem = new LightingSystem();
    scene.add(lightingSystem);

    // Initialize Reflex bridge for state synchronization
    const reflexBridge = new Reflex3DBridge(reflexState, scene);

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        reflexBridge.update(); // Update Reflex state
        renderer.render(scene, camera);
    }

    animate();

    // Handle window resize
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    return {
        scene,
        camera,
        renderer,
        reflexBridge,
    };
}