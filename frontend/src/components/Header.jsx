import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="header">
      <div className="header-left">
        <span className="logo-text">SquidGame</span>
        <span className="logo-ctf">CTF</span>
      </div>
      <div className="header-right">
        <a href="/login" className="login-link">Login</a>
      </div>
    </header>
  );
}

export default Header;
