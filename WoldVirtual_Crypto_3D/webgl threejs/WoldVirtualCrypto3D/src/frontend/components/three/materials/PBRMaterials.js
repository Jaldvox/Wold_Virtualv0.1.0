import * as THREE from 'three';

export const createPBRMaterials = () => {
    const materials = {};

    // Create a basic PBR material
    materials.basicMaterial = new THREE.MeshStandardMaterial({
        color: 0xffffff,
        roughness: 0.5,
        metalness: 0.5,
    });

    // Create a textured PBR material
    materials.texturedMaterial = new THREE.MeshStandardMaterial({
        map: new THREE.TextureLoader().load('/path/to/your/texture.jpg'),
        roughnessMap: new THREE.TextureLoader().load('/path/to/your/roughnessMap.jpg'),
        metalnessMap: new THREE.TextureLoader().load('/path/to/your/metalnessMap.jpg'),
        normalMap: new THREE.TextureLoader().load('/path/to/your/normalMap.jpg'),
        aoMap: new THREE.TextureLoader().load('/path/to/your/aoMap.jpg'),
        transparent: false,
    });

    // Create a glass material
    materials.glassMaterial = new THREE.MeshStandardMaterial({
        color: 0x00ffcc,
        transparent: true,
        opacity: 0.5,
        roughness: 0.1,
        metalness: 0.1,
    });

    return materials;
};