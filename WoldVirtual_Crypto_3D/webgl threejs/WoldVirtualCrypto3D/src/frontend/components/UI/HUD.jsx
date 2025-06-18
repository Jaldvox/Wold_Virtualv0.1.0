import React from 'react';

const HUD = ({ userInfo, sceneInfo }) => {
    return (
        <div className="hud">
            <div className="user-info">
                <h2>User Info</h2>
                <p>Name: {userInfo.name}</p>
                <p>Score: {userInfo.score}</p>
            </div>
            <div className="scene-info">
                <h2>Scene Info</h2>
                <p>Current Scene: {sceneInfo.name}</p>
                <p>Time: {sceneInfo.time}</p>
            </div>
        </div>
    );
};

export default HUD;