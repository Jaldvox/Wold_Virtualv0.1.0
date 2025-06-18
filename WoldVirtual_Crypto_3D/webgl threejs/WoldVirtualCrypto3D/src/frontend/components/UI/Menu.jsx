import React from 'react';

const Menu = ({ onMenuItemClick }) => {
  return (
    <nav className="menu">
      <ul>
        <li onClick={() => onMenuItemClick('home')}>Home</li>
        <li onClick={() => onMenuItemClick('metaverse')}>Metaverse</li>
        <li onClick={() => onMenuItemClick('profile')}>Profile</li>
        <li onClick={() => onMenuItemClick('settings')}>Settings</li>
        <li onClick={() => onMenuItemClick('logout')}>Logout</li>
      </ul>
    </nav>
  );
};

export default Menu;