# Cube

A terminal tool for managing game servers running on [AMP](https://cubecoders.com/AMP) by CubeCoders, without opening the web panel.

Type `cube`, get a live view of every server: what's online, who's playing, and quick controls to start, stop or restart them, plus a live console.

> **Status:** work in progress. I'm building this to learn Python, so expect it in small batches.

## Features

Planned, roughly in the order they'll be built:

- [ ] Log in to AMP with the same account as the web panel
- [ ] List every server with its status (online or offline) and player count
- [ ] Pick a server by number to start, stop or restart it
- [ ] Live console that updates as it happens, with the ability to send commands
- [ ] Extras: player list, backups, performance stats, broadcast messages
- [ ] Spinning 3D ASCII cube animation on launch
- [ ] Run it from anywhere with the `cube` command

## Requirements

- Python 3.11 or newer
- An AMP server, reachable from your machine (I connect to mine over [Tailscale](https://tailscale.com))
- An AMP user account with permission to manage your instances

## Setup

1. Clone the repo and enter it:

   ```sh
   git clone https://github.com/Tregglez/cube.git
   cd cube
   ```

2. Create a virtual environment and install the dependencies:

   ```sh
   python -m venv .venv
   source .venv/bin/activate      # fish: source .venv/bin/activate.fish
   pip install requests rich
   ```

3. Copy the example config to your config folder and fill in your details:

   ```sh
   mkdir -p ~/.config/cube
   cp config.example.toml ~/.config/cube/config.toml
   ```

   Then edit `~/.config/cube/config.toml` with your AMP address and username. Your password isn't stored: Cube asks for it when it starts.

## Usage

Coming soon.

## Why "Cube"?

AMP is made by CubeCoders, and I wanted something quick to check and control my servers from while I'm playing, without opening the browser. 'cube' is short to type and shows the same information.