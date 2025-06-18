class LODManager {
    constructor() {
        this.levelsOfDetail = new Map();
    }

    addLOD(object, lods) {
        this.levelsOfDetail.set(object, lods);
    }

    update(camera) {
        this.levelsOfDetail.forEach((lods, object) => {
            const distance = camera.position.distanceTo(object.position);
            let selectedLOD = lods[0];

            for (let i = 1; i < lods.length; i++) {
                if (distance < lods[i].distance) {
                    selectedLOD = lods[i];
                    break;
                }
            }

            object.traverse((child) => {
                if (child.isMesh) {
                    child.visible = false;
                }
            });

            selectedLOD.mesh.visible = true;
        });
    }
}

export default LODManager;