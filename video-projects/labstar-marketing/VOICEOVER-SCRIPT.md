# Labstar Marketing Video — Voiceover Script

**Total runtime:** ~54 seconds
**Style:** Warm, trustworthy, community-focused. Conversational but professional.

---

## Scene 1 — Title (7s)
*No voiceover — let the visual breathe*

---

## Scene 2 — Problem (10s)

> "When you need lab results, the last thing you want is to wait days, pay hundreds of dollars, or drive across town — only to get a report you don't understand."

---

## Scene 3 — Solution (8s)

> "Labstar is your community diagnostic lab. Walk in or book online — no referral needed. We make professional lab testing fast, affordable, and easy to understand."

---

## Scene 4 — Services (10s)

> "From urinalysis and drug screening to PCR tests and full disease panels — we offer everything you need, all in one place."

---

## Scene 5 — Why Labstar (9s)

> "Results when you need them. Prices that make sense. Clinical-grade accuracy you can trust. That's the Labstar promise."

---

## Scene 6 — CTA (10s)

> "Don't wait. Visit Labstar dot net to book your test today, or call us at 267-791-0272. Your health can't wait — and neither should you."

---

## Generation Notes

```bash
# Generate with ElevenLabs (warm, professional female voice)
python3 tools/voiceover.py \
  --script VOICEOVER-SCRIPT.md \
  --output public/audio/voiceover.mp3 \
  --voice "Rachel" \
  --provider elevenlabs

# Or with Qwen3-TTS (free, local)
python3 tools/voiceover.py \
  --script VOICEOVER-SCRIPT.md \
  --output public/audio/voiceover.mp3 \
  --provider qwen3 \
  --tone warm
```

After generating, add to demo-config.ts:
```typescript
audio: {
  voiceoverFile: 'audio/voiceover.mp3',
  voiceoverStartFrame: 210,  // Start at scene 2 (7s × 30fps)
  backgroundMusicFile: 'audio/background-music.mp3',
  backgroundMusicVolume: 0.1,
},
```
