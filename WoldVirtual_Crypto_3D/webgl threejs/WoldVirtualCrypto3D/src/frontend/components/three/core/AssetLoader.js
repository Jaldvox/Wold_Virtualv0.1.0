class AssetLoader {
    constructor() {
        this.loader = new THREE.GLTFLoader();
        this.assets = {};
    }

    loadModel(url, name) {
        return new Promise((resolve, reject) => {
            this.loader.load(
                url,
                (gltf) => {
                    this.assets[name] = gltf;
                    resolve(gltf);
                },
                undefined,
                (error) => {
                    console.error(`Error loading model ${name}:`, error);
                    reject(error);
                }
            );
        });
    }

    getAsset(name) {
        return this.assets[name];
    }

    clearAssets() {
        this.assets = {};
    }
}

export default AssetLoader;