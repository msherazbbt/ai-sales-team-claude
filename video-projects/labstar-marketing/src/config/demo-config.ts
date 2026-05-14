import type { ProductDemoConfig, VideoConfig } from './types';

export const demoConfig: ProductDemoConfig = {
  product: {
    name: 'Labstar',
    tagline: 'Fast. Affordable. Accurate.',
    website: 'labstar.net',
  },

  scenes: [
    // Title
    {
      type: 'title',
      durationSeconds: 7,
      content: {
        headline: 'Lab Tests.\nFast. Affordable.\nAccurate.',
        subheadline: 'Your Community Diagnostic Lab — labstar.net',
      },
    },

    // Problem
    {
      type: 'problem',
      durationSeconds: 10,
      content: {
        headline: 'Traditional labs let you down',
        problems: [
          { icon: '⏳', text: 'Days of waiting for results' },
          { icon: '💸', text: 'Expensive, unexpected costs' },
          { icon: '📍', text: 'Inconvenient locations & long queues' },
          { icon: '😕', text: 'Confusing results, no clear answers' },
        ],
      },
    },

    // Solution
    {
      type: 'solution',
      durationSeconds: 8,
      content: {
        headline: 'There is a better way.',
        description: 'Labstar brings clinical-grade diagnostic testing to your community — fast, affordable, and stress-free.',
        highlights: [
          'No referral needed — walk in or book online',
          'Results delivered quickly & clearly explained',
          'Transparent, affordable pricing',
        ],
      },
    },

    // Services
    {
      type: 'stats',
      durationSeconds: 10,
      content: {
        headline: 'Everything You Need in One Place',
        stats: [
          { value: '🔬', label: 'Urinalysis', color: '#29A8FF' },
          { value: '💊', label: 'Drug & Toxicity Screening', color: '#00C9A7' },
          { value: '🧬', label: 'PCR Testing', color: '#29A8FF' },
          { value: '🩺', label: 'Disease Panels', color: '#00C9A7' },
        ],
      },
    },

    // Why Labstar
    {
      type: 'stats',
      durationSeconds: 9,
      content: {
        headline: 'Why Thousands Choose Labstar',
        stats: [
          { value: 'FAST', label: 'Same-day results available', icon: '⚡', color: '#29A8FF' },
          { value: 'LOW', label: 'Affordable — no surprise bills', icon: '💚', color: '#00C9A7' },
          { value: '99%', label: 'Clinical-grade accuracy', icon: '🎯', color: '#29A8FF' },
        ],
      },
    },

    // CTA
    {
      type: 'cta',
      durationSeconds: 10,
      content: {
        headline: 'Get Tested Today',
        tagline: 'Affordable diagnostics for your whole community',
        links: [
          { type: 'website', label: 'Visit labstar.net', url: 'labstar.net' },
          { type: 'custom', label: 'Call: (267) 791-0272', url: 'tel:+12677910272' },
        ],
      },
    },
  ],

  audio: {
    backgroundMusicFile: 'audio/background-music.mp3',
    backgroundMusicVolume: 0.1,
  },

  narrator: {
    enabled: false,
    videoFile: 'narrator.mp4',
    position: 'bottom-right',
    size: 'md',
    startFrame: 0,
  },
};

// Video settings
export const videoConfig: VideoConfig = {
  fps: 30,
  width: 1920,
  height: 1080,
};

// Calculate total duration from scenes
export function calculateTotalFrames(config: ProductDemoConfig, fps: number): number {
  return config.scenes.reduce((total, scene) => {
    return total + scene.durationSeconds * fps;
  }, 0);
}
