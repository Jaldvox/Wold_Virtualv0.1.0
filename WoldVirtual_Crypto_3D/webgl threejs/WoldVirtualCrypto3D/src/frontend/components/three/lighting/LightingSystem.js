class LightingSystem {
    constructor(scene) {
        this.scene = scene;
        this.ambientLight = null;
        this.directionalLight = null;
        this.initLights();
    }

    initLights() {
        // Ambient Light
        this.ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Soft white light
        this.scene.add(this.ambientLight);

        // Directional Light
        this.directionalLight = new THREE.DirectionalLight(0xffffff, 1); // Bright white light
        this.directionalLight.position.set(5, 10, 7.5); // Position the light
        this.directionalLight.castShadow = true; // Enable shadows
        this.scene.add(this.directionalLight);

        // Optional: Set up shadow properties for the directional light
        this.directionalLight.shadow.mapSize.width = 1024; // Default
        this.directionalLight.shadow.mapSize.height = 1024; // Default
        this.directionalLight.shadow.camera.near = 0.5; // Default
        this.directionalLight.shadow.camera.far = 50; // Default
        this.directionalLight.shadow.camera.left = -10; // Default
        this.directionalLight.shadow.camera.right = 10; // Default
        this.directionalLight.shadow.camera.top = 10; // Default
        this.directionalLight.shadow.camera.bottom = -10; // Default
    }

    updateLighting() {
        // Update lighting properties if needed
        // This method can be expanded to adjust light intensity, color, etc.
    }
}

export default LightingSystem;