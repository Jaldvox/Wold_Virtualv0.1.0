class SceneManager {
    constructor(renderer, scene, camera) {
        this.renderer = renderer;
        this.scene = scene;
        this.camera = camera;
        this.clock = new THREE.Clock();
        this.mixer = null; // For animations
    }

    init() {
        this.setupRenderer();
        this.setupCamera();
        this.setupLights();
        this.animate();
    }

    setupRenderer() {
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(this.renderer.domElement);
    }

    setupCamera() {
        this.camera.position.set(0, 1, 5);
        this.camera.lookAt(0, 1, 0);
    }

    setupLights() {
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        this.scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
        directionalLight.position.set(5, 10, 7.5);
        this.scene.add(directionalLight);
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        const delta = this.clock.getDelta();

        if (this.mixer) {
            this.mixer.update(delta);
        }

        this.renderer.render(this.scene, this.camera);
    }

    setAnimationMixer(mixer) {
        this.mixer = mixer;
    }

    resize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
}

export default SceneManager;