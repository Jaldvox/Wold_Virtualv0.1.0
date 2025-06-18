import * as THREE from 'three';

class Environment {
    constructor(scene) {
        this.scene = scene;
        this.environment = null;
        this.init();
    }

    init() {
        this.createSkybox();
        this.addGround();
    }

    createSkybox() {
        const loader = new THREE.CubeTextureLoader();
        const texture = loader.load([
            'path/to/px.jpg', // right
            'path/to/nx.jpg', // left
            'path/to/py.jpg', // top
            'path/to/ny.jpg', // bottom
            'path/to/pz.jpg', // back
            'path/to/nz.jpg'  // front
        ]);
        this.scene.background = texture;
    }

    addGround() {
        const geometry = new THREE.PlaneGeometry(1000, 1000);
        const material = new THREE.MeshStandardMaterial({ color: 0x7ec850 });
        const ground = new THREE.Mesh(geometry, material);
        ground.rotation.x = -Math.PI / 2; // Rotate to make it horizontal
        this.scene.add(ground);
    }

    update() {
        // Update environment properties if needed
    }
}

export default Environment;