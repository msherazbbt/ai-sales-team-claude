#!/bin/bash
# ============================================================================
# Claude Code Video Toolkit Installer
# Source: https://github.com/digitalsamba/claude-code-video-toolkit
# ============================================================================
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

TOOLKIT_REPO="https://github.com/digitalsamba/claude-code-video-toolkit.git"

echo ""
echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                              ║${NC}"
echo -e "${BLUE}║${NC}   ${CYAN}Claude Code Video Toolkit${NC}                                  ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}   ${GREEN}Skills · Commands · Python Tools${NC}                          ${BLUE}║${NC}"
echo -e "${BLUE}║                                                              ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# ---------------------------------------------------------------------------
# Clone the toolkit
# ---------------------------------------------------------------------------
echo -e "${BLUE}Cloning video toolkit...${NC}"
TEMP_DIR=$(mktemp -d)
git clone --depth 1 "$TOOLKIT_REPO" "$TEMP_DIR/toolkit" 2>/dev/null
echo -e "  ${GREEN}✓${NC} Cloned from $TOOLKIT_REPO"

# ---------------------------------------------------------------------------
# Install skills to ~/.claude/skills/
# ---------------------------------------------------------------------------
echo -e "${BLUE}Installing skills...${NC}"
mkdir -p "$HOME/.claude/skills"
SKILL_COUNT=0
for skill_dir in "$TEMP_DIR/toolkit/.claude/skills/"/*/; do
    skill_name=$(basename "$skill_dir")
    cp -r "$skill_dir" "$HOME/.claude/skills/$skill_name"
    echo -e "  ${GREEN}✓${NC} $skill_name"
    SKILL_COUNT=$((SKILL_COUNT + 1))
done

# ---------------------------------------------------------------------------
# Install commands to ~/.claude/commands/
# ---------------------------------------------------------------------------
echo -e "${BLUE}Installing commands...${NC}"
mkdir -p "$HOME/.claude/commands"
CMD_COUNT=0
for cmd_file in "$TEMP_DIR/toolkit/.claude/commands/"*.md; do
    cmd_name=$(basename "$cmd_file")
    cp "$cmd_file" "$HOME/.claude/commands/$cmd_name"
    echo -e "  ${GREEN}✓${NC} /${cmd_name%.md}"
    CMD_COUNT=$((CMD_COUNT + 1))
done

# ---------------------------------------------------------------------------
# Install Python dependencies
# ---------------------------------------------------------------------------
echo -e "${BLUE}Installing Python dependencies...${NC}"
if command -v python3 &>/dev/null && command -v pip3 &>/dev/null; then
    pip3 install -r "$TEMP_DIR/toolkit/tools/requirements.txt" -q
    echo -e "  ${GREEN}✓${NC} Python packages installed"
elif command -v pip &>/dev/null; then
    pip install -r "$TEMP_DIR/toolkit/tools/requirements.txt" -q
    echo -e "  ${GREEN}✓${NC} Python packages installed"
else
    echo -e "  ${YELLOW}⚠${NC} pip not found — install Python deps manually:"
    echo -e "      ${CYAN}pip install -r tools/requirements.txt${NC}"
fi

# ---------------------------------------------------------------------------
# Cleanup
# ---------------------------------------------------------------------------
rm -rf "$TEMP_DIR"
echo -e "  ${GREEN}✓${NC} Cleaned up temporary files"

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Video Toolkit Installation Complete!                        ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${CYAN}Skills:${NC}   $SKILL_COUNT installed  →  ~/.claude/skills/"
echo -e "  ${CYAN}Commands:${NC} $CMD_COUNT installed  →  ~/.claude/commands/"
echo ""
echo -e "${BLUE}Available commands (restart Claude Code to load):${NC}"
echo ""
echo -e "  ${CYAN}/setup${NC}              Interactive toolkit configuration"
echo -e "  ${CYAN}/video${NC}              Create or resume a video project"
echo -e "  ${CYAN}/brand${NC}              Manage brand profiles"
echo -e "  ${CYAN}/scene-review${NC}       Review scenes in Remotion Studio"
echo -e "  ${CYAN}/generate-voiceover${NC} Generate AI narration"
echo -e "  ${CYAN}/record-demo${NC}        Record browser interactions"
echo -e "  ${CYAN}/design${NC}             Refine slide visuals"
echo -e "  ${CYAN}/redub${NC}              Redub video with a different voice"
echo ""
echo -e "  ${YELLOW}Tip:${NC} Run ${CYAN}/setup${NC} first to configure cloud GPU and voice settings!"
echo ""
