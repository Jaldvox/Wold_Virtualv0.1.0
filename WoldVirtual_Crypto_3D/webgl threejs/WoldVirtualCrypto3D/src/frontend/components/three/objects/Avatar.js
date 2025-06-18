class Avatar {
    constructor(scene, modelUrl) {
        this.scene = scene;
        this.modelUrl = modelUrl;
        this.avatar = null;
        this.animations = [];
        this.mixer = null;
    }

    async loadModel() {
        const loader = new THREE.GLTFLoader();
        const gltf = await loader.loadAsync(this.modelUrl);
        this.avatar = gltf.scene;
        this.animations = gltf.animations;

        if (this.animations.length) {
            this.mixer = new THREE.AnimationMixer(this.avatar);
            this.animations.forEach((clip) => {
                this.mixer.clipAction(clip).play();
            });
        }

        this.scene.add(this.avatar);
    }

    update(delta) {
        if (this.mixer) {
            this.mixer.update(delta);
        }
    }

    setPosition(position) {
        if (this.avatar) {
            this.avatar.position.set(position.x, position.y, position.z);
        }
    }

    setRotation(rotation) {
        if (this.avatar) {
            this.avatar.rotation.set(rotation.x, rotation.y, rotation.z);
        }
    }

    onClick(callback) {
        if (this.avatar) {
            this.avatar.traverse((child) => {
                if (child.isMesh) {
                    child.userData.clickable = true;
                    child.onClick = callback;
                }
            });
        }
    }
}

export default Avatar;