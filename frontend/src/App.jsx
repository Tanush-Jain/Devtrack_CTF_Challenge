import React from 'react';
import Header from './components/Header';
import MainContent from './components/MainContent';
import FeatureBlocks from './components/FeatureBlocks';
import Footer from './components/Footer';
import SquidGameBackground from './components/SquidGameBackground';
import './App.css';

function App() {
  return (
    <div className="app">
      <SquidGameBackground />
      <div className="content-overlay">
        <Header />
        <MainContent />
        <FeatureBlocks />
        <Footer />
      </div>
    </div>
  );
}

export default App;
