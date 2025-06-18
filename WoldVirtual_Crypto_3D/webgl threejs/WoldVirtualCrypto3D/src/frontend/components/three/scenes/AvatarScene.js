import * as THREE from 'three';
import { useEffect, useRef } from 'react';
import { useFrame } from '@react-three/fiber';
import Avatar from '../objects/Avatar';
import { useReflexState } from '../../../hooks/useReflexState';

const AvatarScene = () => {
    const avatarRef = useRef();
    const { state, updateState } = useReflexState();

    useEffect(() => {
        // Initialize the avatar and set its position based on state
        if (avatarRef.current) {
            avatarRef.current.position.set(
                state.avatarPosition.x,
                state.avatarPosition.y,
                state.avatarPosition.z
            );
        }
    }, [state.avatarPosition]);

    useFrame(() => {
        // Update avatar animations or interactions here
        if (avatarRef.current) {
            avatarRef.current.updateAnimation();
        }
    });

    const handleAvatarClick = () => {
        // Handle avatar click event and update state
        updateState({ selectedAvatar: avatarRef.current.id });
    };

    return (
        <group>
            <Avatar ref={avatarRef} onClick={handleAvatarClick} />
        </group>
    );
};

export default AvatarScene;