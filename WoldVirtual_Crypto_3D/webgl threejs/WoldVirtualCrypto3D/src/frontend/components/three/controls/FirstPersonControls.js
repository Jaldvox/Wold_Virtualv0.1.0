import * as THREE from 'three';

class FirstPersonControls {
    constructor(camera, domElement) {
        this.camera = camera;
        this.domElement = domElement;

        this.movementSpeed = 1.0;
        this.lookSpeed = 0.1;

        this.pitchObject = new THREE.Object3D();
        this.pitchObject.add(this.camera);

        this.yawObject = new THREE.Object3D();
        this.yawObject.add(this.pitchObject);

        this.moveForward = false;
        this.moveBackward = false;
        this.moveLeft = false;
        this.moveRight = false;

        this.mouseX = 0;
        this.mouseY = 0;

        this.init();
    }

    init() {
        this.domElement.addEventListener('mousemove', this.onMouseMove.bind(this), false);
        this.domElement.addEventListener('mousedown', this.onMouseDown.bind(this), false);
        this.domElement.addEventListener('mouseup', this.onMouseUp.bind(this), false);
        this.domElement.addEventListener('keydown', this.onKeyDown.bind(this), false);
        this.domElement.addEventListener('keyup', this.onKeyUp.bind(this), false);
    }

    onMouseMove(event) {
        this.mouseX = event.clientX;
        this.mouseY = event.clientY;
    }

    onMouseDown(event) {
        // Handle mouse down events for interactions
    }

    onMouseUp(event) {
        // Handle mouse up events for interactions
    }

    onKeyDown(event) {
        switch (event.code) {
            case 'KeyW':
                this.moveForward = true;
                break;
            case 'KeyS':
                this.moveBackward = true;
                break;
            case 'KeyA':
                this.moveLeft = true;
                break;
            case 'KeyD':
                this.moveRight = true;
                break;
        }
    }

    onKeyUp(event) {
        switch (event.code) {
            case 'KeyW':
                this.moveForward = false;
                break;
            case 'KeyS':
                this.moveBackward = false;
                break;
            case 'KeyA':
                this.moveLeft = false;
                break;
            case 'KeyD':
                this.moveRight = false;
                break;
        }
    }

    update(delta) {
        const moveDistance = this.movementSpeed * delta;

        if (this.moveForward) this.camera.position.z -= moveDistance;
        if (this.moveBackward) this.camera.position.z += moveDistance;
        if (this.moveLeft) this.camera.position.x -= moveDistance;
        if (this.moveRight) this.camera.position.x += moveDistance;

        const lookDirection = new THREE.Vector3();
        lookDirection.setFromMatrixColumn(this.camera.matrix, 0);
        lookDirection.y = 0;
        lookDirection.normalize();

        const yawAngle = this.lookSpeed * (this.mouseX - window.innerWidth / 2);
        const pitchAngle = this.lookSpeed * (this.mouseY - window.innerHeight / 2);

        this.yawObject.rotation.y -= yawAngle;
        this.pitchObject.rotation.x -= pitchAngle;

        this.camera.lookAt(this.camera.position.clone().add(lookDirection));
    }
}

export default FirstPersonControls;