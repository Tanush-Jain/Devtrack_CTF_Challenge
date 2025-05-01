import React from 'react';
import './MainContent.css';

function MainContent() {
  return (
    <main className="main-content">
      <div className="left-side">
        <h1 className="title">
          <span className="squidgame">SquidGame</span> <span className="ctf">CTF</span>
          <span className="triangle-icon" aria-hidden="true">▶</span>
        </h1>
        <p className="description">
          Enter the world of SquidGame CTF, where every challenge tests your wit and skill. Join the ultimate cybersecurity battle and prove your mastery.
        </p>
        <div className="portal-buttons">
          <a href="/admin" className="portal-button admin-button">Admin Portal</a>
          <a href="/participant" className="portal-button participant-button">Participant Portal</a>
        </div>
      </div>
      <div className="right-side">
        <div className="image-container">
          {/* Placeholder image: place your 3D guard image at /public/images/squidgame_guard.png */}
          <img
            src="/images/squidgame_guard.png"
            alt="3D Squid Game Guard"
            className="guard-image"
          />
        </div>
      </div>
    </main>
  );
}

export default MainContent;
