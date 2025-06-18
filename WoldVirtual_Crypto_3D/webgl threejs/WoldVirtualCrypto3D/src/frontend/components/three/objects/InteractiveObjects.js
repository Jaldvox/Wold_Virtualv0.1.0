class InteractiveObjects {
    constructor(scene) {
        this.scene = scene;
        this.interactiveObjects = [];
    }

    addInteractiveObject(object) {
        this.interactiveObjects.push(object);
        this.scene.add(object);
    }

    removeInteractiveObject(object) {
        const index = this.interactiveObjects.indexOf(object);
        if (index > -1) {
            this.interactiveObjects.splice(index, 1);
            this.scene.remove(object);
        }
    }

    handleInteraction(raycaster, mouse) {
        const intersects = raycaster.intersectObjects(this.interactiveObjects);
        if (intersects.length > 0) {
            const object = intersects[0].object;
            this.onObjectClick(object);
        }
    }

    onObjectClick(object) {
        // Implement the logic for what happens when an object is clicked
        console.log('Object clicked:', object);
    }
}

export default InteractiveObjects;