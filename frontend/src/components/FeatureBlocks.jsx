import React from 'react';
import './FeatureBlocks.css';

const features = [
  {
    title: 'Challenging Puzzles',
    description: 'Engage with complex and thematic puzzles inspired by Squid Game.',
  },
  {
    title: 'Real-time Scoreboard',
    description: 'Track your progress and compete with others in real-time.',
  },
  {
    title: 'Immersive Experience',
    description: 'Dive into a fully themed environment with animations and effects.',
  },
];

function FeatureBlock({ title, description }) {
  return (
    <div className="feature-block">
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function FeatureBlocks() {
  return (
    <section className="feature-blocks-section">
      <div className="feature-blocks-container">
        {features.map((feature, index) => (
          <FeatureBlock key={index} title={feature.title} description={feature.description} />
        ))}
      </div>
    </section>
  );
}

export default FeatureBlocks;
