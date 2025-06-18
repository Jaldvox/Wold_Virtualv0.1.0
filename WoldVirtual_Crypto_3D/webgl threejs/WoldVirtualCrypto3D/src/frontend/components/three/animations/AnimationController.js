class AnimationController {
    constructor() {
        this.animations = {};
        this.mixer = null;
    }

    addAnimation(name, animation) {
        this.animations[name] = animation;
    }

    setMixer(mixer) {
        this.mixer = mixer;
    }

    playAnimation(name) {
        if (this.mixer && this.animations[name]) {
            const action = this.mixer.clipAction(this.animations[name]);
            action.play();
        }
    }

    update(delta) {
        if (this.mixer) {
            this.mixer.update(delta);
        }
    }

    stopAnimation(name) {
        if (this.mixer && this.animations[name]) {
            const action = this.mixer.clipAction(this.animations[name]);
            action.stop();
        }
    }
}

export default AnimationController;