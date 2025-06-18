import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

class ThirdPersonControls {
    constructor(camera, domElement) {
        this.camera = camera;
        this.domElement = domElement;

        this.target = new THREE.Vector3(0, 0, 0);
        this.distance = 5;
        this.theta = 0;
        this.phi = 0;

        this.controls = new OrbitControls(this.camera, this.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.25;
        this.controls.screenSpacePanning = false;

        this.updateCameraPosition();
    }

    updateCameraPosition() {
        this.camera.position.x = this.target.x + this.distance * Math.sin(this.phi) * Math.cos(this.theta);
        this.camera.position.y = this.target.y + this.distance * Math.sin(this.theta);
        this.camera.position.z = this.target.z + this.distance * Math.cos(this.phi) * Math.cos(this.theta);
        this.camera.lookAt(this.target);
    }

    setTarget(target) {
        this.target.copy(target);
        this.updateCameraPosition();
    }

    setDistance(distance) {
        this.distance = distance;
        this.updateCameraPosition();
    }

    setAngles(theta, phi) {
        this.theta = theta;
        this.phi = phi;
        this.updateCameraPosition();
    }

    update() {
        this.controls.update();
    }
}

export default ThirdPersonControls;